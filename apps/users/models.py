from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from phonenumber_field.modelfields import PhoneNumberField
from image_cropping import ImageRatioField, ImageCropField

from .managers import UserAccountManager

# Create your models here.

# ------------------------
class TalentAccount(AbstractBaseUser):
    name                = models.CharField(max_length=100)
    email               = models.EmailField(verbose_name='email', max_length=70, unique=True)
    phone               = PhoneNumberField(null=True)
    profile_picture     = models.ImageField(upload_to='profile_pictures', blank=True, null=True, default='profile_pictures/default_profile_picture.png')
    profile_picture_b2  = models.CharField(max_length=200, null=True, blank=True, default="https://f005.backblazeb2.com/file/picteame-dev/defaults/default_profile_picture.png")
    city                = models.ForeignKey('core.ProxyCity', on_delete=models.SET_NULL, null=True, blank=True)
    categories          = models.ManyToManyField('core.Category', null=True)
    contact_email       = models.EmailField(verbose_name='contact_email', max_length=70, unique=False, null=True)
    contact_phone       = PhoneNumberField(null=True)
    contact_instagram   = models.CharField(max_length=50, null=True)

    greeting            = models.TextField(null=True)

    # fees              = added as a one-to-many relationship in core.Fee
    # photos            = added as a one-to-many relationship in core.Photo

    created_at      = models.DateTimeField(verbose_name='created_at', auto_now_add=True)
    last_login      = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = []

    objects = UserAccountManager()

    def __str__(self):
        return '%s | %s' % (self.email, self.name)

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return True
