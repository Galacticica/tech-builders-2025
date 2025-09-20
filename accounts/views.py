"""
File: views.py
Author: Reagan Zierke <reaganzierke@gmail.com>
Date: 2025-09-20
Description: Views for user authentication and profile management.
"""



from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.views import View
from .forms import LoginForm, SignupForm
from community_projects.models import CommunityProject
from events.models import Event
from creations.models import Creation


User = get_user_model()

class MyLoginView(LoginView):
    form_class = LoginForm
    template_name = "accounts/login.html"
    redirect_authenticated_user = True

class MySignupView(FormView):
    form_class = SignupForm
    template_name = "accounts/signup.html"
    success_url = "/" 

    def form_valid(self, form):
        user = User.objects.create(
            email=form.cleaned_data["email"],
            first_name=form.cleaned_data["first_name"],
            last_name=form.cleaned_data["last_name"],
            password=make_password(form.cleaned_data["password"]),
        )
        login(self.request, user)
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

class MyLogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)  
        return redirect("/")  


def profile_view(request, user_id=None):
    if user_id:
        user = get_object_or_404(User, id=user_id)
    else:
        if not request.user.is_authenticated:
            return redirect("login")
        user = request.user

    events = Event.objects.filter(author=user)
    projects = CommunityProject.objects.filter(author=user)
    creations = Creation.objects.filter(author=user)

    return render(request, "accounts/profile.html", {
        "profile_user": user,
        "events": events,
        "projects": projects,
        "creations": creations,
    })
    

