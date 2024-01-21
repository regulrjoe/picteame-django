from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.conf import Settings
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .decorators import unauthenticated_user
from .forms import RegisterForm, LoginForm
from .models import TalentAccount
from django.views.generic.base import View


# ----------------------
@unauthenticated_user
def register_view(request):
    context = {}
    form = RegisterForm()
    if request.POST:
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)

            login(request, user)
            return redirect(reverse('profile_picture_uploader'))

    context['register_form'] = form

    return render(request, 'users/register.html', context)

# ----------------------
@unauthenticated_user
def login_view(request):
    context = {}
    form = LoginForm()
    if request.POST:
        form = LoginForm(request.POST)
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Wrong Username/Password combination.')

    context['login_form'] = form
    return render(request, 'users/login.html', context)


# ----------------------
def logout_view(request):
    logout(request)
    return redirect('home')

def profile_picture_uploader_view(request):
    context = {}
    form = UploadAndCropProfilePictureForm()
    if request.POST:
        form = UploadAndCropProfilePictureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    context['form'] = form
    return render(request, 'users/profile_picture_uploader.html', context)