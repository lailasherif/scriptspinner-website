from datetime import date, datetime, timedelta
import logging
import stripe
from .models import ScriptSpinnerUser
from django.conf import settings

MONTH = 'm'
ANNUAL = 'a'

API_KEY = settings.STRIPE_SECRET_KEY
logger = logging.getLogger(__name__)

class SS_MonthPlan:
    def __init__(self):
        self.stripe_plan_id = settings.STRIPE_PLAN_MONTHLY_ID
        self.amount = 1000


class SS_AnnualPlan:
    def __init__(self):
        self.stripe_plan_id = settings.STRIPE_PLAN_ANNUAL_ID
        self.amount = 12000


class SS_Plan:
    def __init__(self, plan_id):
        """
        plan_id is either string 'm' (stands for monthly)
        or a string letter 'a' (which stands for annual)
        """
        if plan_id == MONTH:
            self.plan = SS_MonthPlan()
            self.id = MONTH
        elif plan_id == ANNUAL:
            self.plan = SS_AnnualPlan()
            self.id = ANNUAL
        else:
            raise ValueError('Invalid plan_id value')

        self.currency = 'usd'

    @property
    def stripe_plan_id(self):
        return self.plan.stripe_plan_id

    @property
    def amount(self):
        return self.plan.amount


def set_paid_until(charge):
    logger.info(f"Webhook Log: set_paid_until with {charge}")

    stripe.api_key = API_KEY
    pi = stripe.PaymentIntent.retrieve(charge.payment_intent)

    logger.info(f"Webhook Log: pi with {pi}")

    if pi.customer:
        customer = stripe.Customer.retrieve(pi.customer, expand=['subscriptions'])
        logger.info(f"Webhook Log: Customer retrieve {customer}")
        email = customer.email

        if customer:
            subscr = stripe.Subscription.retrieve(
                customer['subscriptions'].data[0].id
            )
            current_period_end = subscr['current_period_end']

        try:
            user = ScriptSpinnerUser.objects.get(email=email)
        except ScriptSpinnerUser.DoesNotExist:
            logger.warning(
                f"User with email {email} not found"
            )
            return False

        user.set_paid_until(current_period_end)
        logger.info(
            f"Profile with {current_period_end} saved for user {email}"
        )
    else:
        email = charge.receipt_email
        amount = charge.amount
        paid = charge.paid

        try:
            user = ScriptSpinnerUser.objects.get(email=email)
        except ScriptSpinnerUser.DoesNotExist:
            logger.warning(
                f"User with email {email} not found"
            )
            return False

        if amount == 1000 and paid:
            user.set_paid_until(date.today() + timedelta(days=31))
        elif amount == 12000 and paid:
            user.set_paid_until(date.today() + timedelta(days=365))
        else:
            logger.warning(f"Not paid or invalid amount: {amount}")