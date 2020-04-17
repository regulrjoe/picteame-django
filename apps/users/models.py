from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField

from .managers import CustomUserManager

# Create your models here.
# ------------------------
class City(models.Model):
    city = models.CharField('City', max_length=100)
    state = models.CharField('State', max_length=100)
    country = CountryField(default='MX')

    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.city  + ', ' + self.state + ' ' + self.country.code

# ------------------------
class Address(models.Model):
    address1 = models.CharField('Address line 1', max_length=250)
    address2 = models.CharField('Address line 2', max_length=250, null=True)
    zip_code = models.CharField('ZIP Code', max_length=12)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.address1 + ', ' + self.address2 + ' ' + self.city


# ------------------------
class CustomUser(AbstractBaseUser):
    name            = models.CharField(max_length=100)
    email           = models.EmailField(verbose_name='email', max_length=70, unique=True)
    username        = models.CharField(max_length=30, unique=True)
    phone           = PhoneNumberField(null=True)
    city            = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)

    date_joined     = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login      = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)

    USERNAME_FIELD  = 'email'

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
