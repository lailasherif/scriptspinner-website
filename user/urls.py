from django.urls import path
from . import views

urlpatterns = [
    path('redirect_to_login/', views.redirect_to_login, name='redirect_to_login'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('stripe-webhooks/', views.stripe_webhooks, name='stripe_webhooks'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('payment_method/', views.payment_method, name='payment_method'),
    path('card/', views.card, name='card'),
]