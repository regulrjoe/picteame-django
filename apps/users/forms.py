from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from image_cropping import ImageCropWidget

from .models import TalentAccount

# ----------------------------
class RegisterForm(UserCreationForm):

    class Meta:
        model = TalentAccount
        fields = ['name', 'city', 'email', 'password1', 'password2']

# ----------------------------
class LoginForm(forms.ModelForm):

    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = TalentAccount
        fields = ['email', 'password']

class ProfilePictureUploadForm(forms.ModelForm):
    class Meta:
        model = TalentAccount
        fields = ['profile_picture']