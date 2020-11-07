import json
import stripe
import logging
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings

from .forms import RegisterForm, LoginForm
from .stripe import SS_Plan, set_paid_until

API_KEY = settings.STRIPE_SECRET_KEY
logger = logging.getLogger(__name__)

@require_POST
@csrf_exempt
def stripe_webhooks(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SIGNING_KEY
        )
        logger.info("Event constructed correctly")
    except ValueError:
        # Invalid payload
        logger.warning("Invalid Payload")
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        # Invalid signature
        logger.warning("Invalid signature")
        return HttpResponse(status=400)

    # Handle the event
    if event.type == 'charge.succeeded':
        # object has  payment_intent attr
        set_paid_until(event.data.object)

    return HttpResponse(status=200)

def redirect_to_login(request):
    if request.user.is_anonymous:
        messages.info(request, 'You must log in to view this page.')
    return redirect('login')

def register(request):
    if request.user.is_authenticated:
        # messages.success(request, 'You are already logged in.')
        return redirect('index')

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New user has been created!')
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form':form})

def login(request):
    if request.user.is_authenticated:
        # messages.info(request, 'You are already logged in.')
        return redirect('index')

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            email = data['email']
            password = data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('index')
        messages.info(request, 'Email address OR password is incorrect')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form':form})

@login_required(login_url='redirect_to_login')
def logout(request):
    auth_logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return redirect('login')

@login_required(login_url='redirect_to_login')
def subscribe(request):
    logger.info("subscribe")
    return render(request, 'payments/subscribe.html')

@require_POST
@login_required
def payment_method(request):
    stripe.api_key = API_KEY
    plan = request.POST.get('plan')
    automatic = request.POST.get('automatic')
    payment_method = request.POST.get('payment_method')
    context = {}

    plan_inst = SS_Plan(plan_id=plan)

    payment_intent = stripe.PaymentIntent.create(
        amount=plan_inst.amount,
        currency=plan_inst.currency,
        payment_method_types=['card']
    )

    if payment_method == 'card':

        context['secret_key'] = payment_intent.client_secret
        context['STRIPE_PUBLISHABLE_KEY'] = settings.STRIPE_PUBLISHABLE_KEY
        context['customer_email'] = request.user.email
        context['payment_intent_id'] = payment_intent.id
        context['automatic'] = automatic
        context['stripe_plan_id'] = plan_inst.stripe_plan_id

        return render(request, 'payments/card.html', context)

    elif payment_method == 'paypal':
        pass

@login_required
def card(request):
    payment_intent_id = request.POST['payment_intent_id']
    payment_method_id = request.POST['payment_method_id']
    stripe_plan_id = request.POST['stripe_plan_id']
    automatic = request.POST['automatic']
    stripe.api_key = API_KEY

    if automatic == 'on':
        customer = stripe.Customer.create(
            email=request.user.email,
            payment_method=payment_method_id,
            invoice_settings={
                'default_payment_method': payment_method_id
            }
        )

        s = stripe.Subscription.create(
            customer=customer.id,
            items=[
                {
                    'plan': stripe_plan_id
                },
            ]
        )

        latest_invoice = stripe.Invoice.retrieve(s.latest_invoice)

        ret = stripe.PaymentIntent.retrieve(
            latest_invoice.payment_intent
        )

        if ret.status == 'requires_action':
            pi = stripe.PaymentIntent.retrieve(
                latest_invoice.payment_intent
            )
            context = {}

            context['payment_intent_secret'] = pi.client_secret
            context['STRIPE_PUBLISHABLE_KEY'] = settings.STRIPE_PUBLISHABLE_KEY

            return render(request, 'payments/3dsec.html', context)

    else:
        stripe.PaymentIntent.modify(
            payment_intent_id,
            payment_method=payment_method_id
        )
        ret = stripe.PaymentIntent.confirm(
            payment_intent_id
        )

        if ret.status == 'requires_action':
            context = {}

            context['payment_intent_secret'] = ret.client_secret
            context['STRIPE_PUBLISHABLE_KEY'] = settings.STRIPE_PUBLISHABLE_KEY

            return render(request, 'payments/3dsec.html', context)

    return render(request, 'payments/thank_you.html')