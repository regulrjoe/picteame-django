from django.db import models
from apps.users.models import UserAccount

# Create your models here.

# -----------------------
class Subscriber(models.Model):
    user        = models.OneToOneField(UserAccount, null=True, on_delete=models.CASCADE)
    email       = models.EmailField(max_length=70, unique=True)
    conf_num    = models.CharField(max_length=15)
    confirmed   = models.BooleanField(default=False)

    def __str__(self):
        return self.email + " (" + ("not " if not self.confirmed else "") + "confirmed)"
