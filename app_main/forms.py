from django.forms import ModelForm
from django import forms

from app_customer.models import Customer
from app_talent.models import Talent

# ----------------------------
class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user'] # Don't edit the user info

# ----------------------------
class TalentForm(ModelForm):
    class Meta:
        model = Talent
        fields = '__all__'
        exclude = ['user'] # Don't edit the user info
