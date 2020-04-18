from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from .models import UserAccount

# ----------------------------
class RegisterForm(UserCreationForm):

    class Meta:
        model = UserAccount
        fields = ['email', 'username', 'password1', 'password2']

# ----------------------------
class LoginForm(forms.ModelForm):

    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = UserAccount
        fields = ['email', 'password']
