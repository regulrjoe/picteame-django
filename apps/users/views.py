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
from .forms import RegisterForm, LoginForm, TalentEditForm
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

    if request.POST:
        talent_form = TalentEditForm(request.POST, request.FILES, instance=request.user)
        if talent_form.is_valid():
            ig = request.user.contact_instagram

            if ig and ig[0] == '@':
                request.user.contact_instagram = ig[1:]

            talent_form.save()
            return redirect('talent_profile', user_id=request.user.id)
    else:
        talent_form = TalentEditForm(instance=request.user)

    context['talent_form'] = talent_form

    return render(request, 'users/talent_edit.html', context)


@login_required
def talent_edit_photos_view(request):
    context = {}

    PhotoFormSet = inlineformset_factory(TalentAccount, Photo, fields=('image', 'categories'), extra=6, can_delete=True, max_num=6, validate_max=True)
    PhotoFormSet.form.base_fields['categories'].required = False

    if request.method == 'POST':
        formset = PhotoFormSet(request.POST, request.FILES, instance=request.user)
        if formset.is_valid():
            print('formset is valid')
            formset.save()
            return redirect('talent_profile', user_id=request.user.id)
    else:
        formset = PhotoFormSet(instance=request.user)
        context = {'photos_formset': formset}
        
    return render(request, 'users/talent_photos_edit.html', context)