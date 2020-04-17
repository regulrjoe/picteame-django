from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from .models import CustomUser

# ----------------------------
class RegisterForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password1', 'password2']

# ----------------------------
class LoginForm(forms.ModelForm):

    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['email', 'password']
