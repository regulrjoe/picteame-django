from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.forms import inlineformset_factory

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model

from django.conf import Settings
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .decorators import unauthenticated_user
from .forms import RegisterForm, LoginForm, TalentEditForm, TalentPhotosForm, get_photos_formset
from .models import TalentAccount
from apps.core.models import Photo
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
            return redirect(reverse('talent_profile', kwargs={'user_id': user.id}))

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
def talent_view(request, user_id):
    user = get_object_or_404(TalentAccount, pk=user_id)
    return render(request, 'users/talent_profile.html', {'user': user})


@login_required
def talent_edit_view(request):
    context = {}

    TalentPhotosFormset = get_photos_formset(TalentPhotosForm, extra=0, can_delete=True, max_num=5, min_num=1)

    photos_qs = request.user.photo_set.all()

    # photos = []
    # for photo in photos_qs:
    photos = [photo.image for photo in photos_qs]

    if request.POST:

        print("POST Request")


        talent_form = TalentEditForm(request.POST, request.FILES, instance=request.user)
        photos_formset = TalentPhotosFormset(request.POST, request.FILES, instance=request.user)

        print(photos_formset.prefix)
        
        if talent_form.is_valid() and photos_formset.is_valid():

            print("Forms are valid")

            ig = request.user.contact_instagram

            if ig and ig[0] == '@':
                request.user.contact_instagram = ig[1:]

            talent_form.save()
            photos_formset.save()

            print("Forms are saved")
            
            return redirect('talent_profile', user_id=request.user.id)

        if talent_form.is_valid() and not photos_formset.is_valid():
            print("Talent form is valid but photos form is not valid")
        elif not talent_form.is_valid() and photos_formset.is_valid():
            print(photos_formset.errors)
            print("Talent form is not valid but photos form is valid")

    talent_form = TalentEditForm(instance=request.user)
    photos_formset = TalentPhotosFormset(instance=request.user)

    context['talent_form'] = talent_form
    context['photos_formset'] = photos_formset
    context['photos'] = photos

    return render(request, 'users/talent_edit.html', context)
