from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model

from django.conf import Settings
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .decorators import unauthenticated_user
from .forms import RegisterForm, LoginForm, ProfilePictureUploadForm, TalentEditForm
from .models import TalentAccount
from django.views.generic.base import View
from django.contrib.auth import get_user
from django.shortcuts import redirect


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
@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

# ----------------------
@login_required
def profile_picture_upload_view(request):
    context = {}

    if request.POST:
        form = ProfilePictureUploadForm(request.POST, request.FILES, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = ProfilePictureUploadForm(instance=request.user)

    context['profile_picture_uploader_form'] = form
    return render(request, 'users/profile_picture_uploader.html', context)

# ----------------------
def talent_view(request, user_id):
    user = get_object_or_404(TalentAccount, pk=user_id)
    return render(request, 'users/talent_profile.html', {'user': user})


@login_required
def talent_edit_view(request):
    context = {}

    # user = get_user(request)

    if request.POST:
        talent_form = TalentEditForm(request.POST, request.FILES, instance=request.user)

        if talent_form.is_valid():

            if request.user.contact_instagram[0] == '@':
                request.user.contact_instagram = request.user.contact_instagram[1:]

            talent_form.save()
            
            return redirect('talent_profile', user_id=request.user.id)

    else:
        talent_form = TalentEditForm(instance=request.user)

    context['talent_form'] = talent_form

    return render(request, 'users/talent_edit.html', context)
