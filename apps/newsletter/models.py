from django.db import models
from apps.users.models import TalentAccount

# Create your models here.

# -----------------------
class Subscriber(models.Model):
    user        = models.OneToOneField('users.TalentAccount', null=True, on_delete=models.CASCADE)
    email       = models.EmailField(max_length=70, unique=True)
    conf_num    = models.CharField(max_length=15)
    confirmed   = models.BooleanField(default=False)
    is_talent   = models.BooleanField(default=False)

    def __str__(self):
        return self.email + " (" + ("not " if not self.confirmed else "") + "confirmed)"
