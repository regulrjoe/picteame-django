from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from phonenumber_field.modelfields import PhoneNumberField
from apps.core.models import Address, City, CustomerProfile, TalentProfile

from .managers import UserAccountManager

# Create your models here.

# ------------------------
class UserAccount(AbstractBaseUser):
    name                = models.CharField(max_length=100)
    email               = models.EmailField(verbose_name='email', max_length=70, unique=True)
    username            = models.CharField(max_length=30, unique=True)
    phone               = PhoneNumberField(null=True)
    profile_picture     = models.ImageField(default="logo.png", blank=True, null=True)
    city                = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    customer_profile    = models.OneToOneField(CustomerProfile, null=True, on_delete=models.CASCADE)
    talent_profile      = models.OneToOneField(TalentProfile, null=True, on_delete=models.CASCADE)

    date_joined     = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login      = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)
    is_talent       = models.BooleanField(default=False)

    USERNAME_FIELD  = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserAccountManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
