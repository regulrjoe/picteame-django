from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from image_cropping import ImageCropWidget

from .models import TalentAccount
from apps.core.models import Category

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

class TalentEditForm(forms.ModelForm):
    name = forms.CharField(required=False, )
    profile_picture = forms.ImageField(required=False)
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)
    contact_email = forms.EmailField(required=False)
    contact_phone = forms.CharField(required=False)
    contact_website = forms.URLField(required=False)
    contact_instagram = forms.CharField(required=False)
    fees = forms.CharField(required=False)

    class Meta:
        model = TalentAccount
        fields = ['name', 'city', 'profile_picture', 
                  'categories', 
                  'contact_email', 'contact_phone', 'contact_website', 'contact_instagram']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance:
            self.fields['name'].initial = instance.name
            self.fields['city'].initial = instance.city
            self.fields['profile_picture'].initial = instance.profile_picture
            self.fields['categories'].initial = instance.categories
            self.fields['contact_email'].initial = instance.contact_email
            self.fields['contact_phone'].initial = instance.contact_phone
            self.fields['contact_website'].initial = instance.contact_website
            self.fields['contact_instagram'].initial = instance.contact_instagram
