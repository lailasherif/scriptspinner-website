from django.urls import path
from . import views

urlpatterns = [
    path('redirect_to_login/', views.redirect_to_login, name='redirect_to_login'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]