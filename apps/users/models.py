from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from phonenumber_field.modelfields import PhoneNumberField
from image_cropping import ImageRatioField

from .managers import UserAccountManager

# Create your models here.

# ------------------------
class TalentAccount(AbstractBaseUser):
    name                = models.CharField(max_length=100)
    email               = models.EmailField(verbose_name='email', max_length=70, unique=True)
    phone               = PhoneNumberField(null=True)
    profile_picture     = models.ImageField(default="logo.png", upload_to='profile_pictures', blank=True, null=True)
    city                = models.ForeignKey('core.City', on_delete=models.SET_NULL, null=True)
    categories          = models.ManyToManyField('core.Category', null=True)
    pp_cropping = ImageRatioField('profile_picture', '430x430')
    # fees              = added as a one-to-many relationship in core.Fee
    # photos            = added as a one-to-many relationship in core.Photo

    date_joined     = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login      = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = []

    objects = UserAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
