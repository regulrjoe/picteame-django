from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from image_cropping import ImageCropWidget
from django.forms import fields, models, formsets, widgets


from .models import TalentAccount
from apps.core.models import Category, Photo

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

class TalentEditForm(forms.ModelForm):
    name = forms.CharField(required=False, )
    profile_picture = forms.ImageField(required=False)
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)
    greeting = forms.TextInput()
    contact_email = forms.EmailField(required=False)
    contact_phone = forms.CharField(required=False)
    contact_website = forms.URLField(required=False)
    contact_instagram = forms.CharField(required=False)

    class Meta:
        model = TalentAccount
        fields = ['profile_picture',
                  'name', 'city',
                  'categories', 
                  'greeting',
                  'contact_email', 
                  'contact_phone', 
                  'contact_website', 
                  'contact_instagram']

class TalentPhotosForm(forms.ModelForm):
    image = forms.ImageField(required=True)
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)

    class Meta:
        model = Photo
        fields = ['image', 'categories', 'talent']

def get_photos_formset(form, formset=models.BaseInlineFormSet, **kwargs):
    return models.inlineformset_factory(TalentAccount, Photo, form, formset, **kwargs)