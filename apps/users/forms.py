from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from image_cropping import ImageCropWidget
from django.forms import fields, models, formsets, widgets


from .models import TalentAccount
from apps.core.models import Category, Photo

# ----------------------------
class RegisterForm(UserCreationForm):
    name = forms.CharField(required=True, label="Nombre")
    email = forms.EmailField(required=True, label="Correo Electrónico")

    class Meta:
        model = TalentAccount
        fields = ['name', 'city', 'email', 'password1', 'password2']
        widgets = {
            'city': forms.Select()
        }
        labels = {
            'city': 'Ciudad'
        }

# ----------------------------
class LoginForm(forms.ModelForm):

    class Meta:
        model = TalentAccount
        fields = ['email', 'password']

class TalentEditForm(forms.ModelForm):
    name = forms.CharField(required=False, label="Nombre")
    profile_picture = forms.ImageField(required=False)
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)
    greeting = forms.CharField(
        max_length=400,
        widget=forms.Textarea(attrs={'rows': 4}),
        required=False)
    contact_email = forms.EmailField(required=False)
    contact_phone = forms.CharField(required=False)
    contact_instagram = forms.CharField(required=False)

    class Meta:
        model = TalentAccount
        fields = [
                  'profile_picture_b2',
                  'name', 
                  'city',
                  'categories', 
                  'greeting',
                  'contact_email', 
                  'contact_phone', 
                  'contact_instagram']