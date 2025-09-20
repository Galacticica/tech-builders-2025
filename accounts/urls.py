"""
File: urls.py
Author: Reagan Zierke <reaganzierke@gmail.com>
Date: 2025-09-20
Description: URL configurations for account-related views.
"""



from django.urls import path
from .views import MyLoginView, MySignupView, MyLogoutView, profile_view


urlpatterns = [
    path("login/", MyLoginView.as_view(), name="login_page"),
    path("signup/", MySignupView.as_view(), name="signup_page"),
    path("logout/", MyLogoutView.as_view(), name="logout_page"),
    path("profile/", profile_view, name="my_profile"),
    path("profile/<int:user_id>/", profile_view, name="user_profile"),
]
