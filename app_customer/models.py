from django.db import models

# Create your models here.

# ------------------------
class Customer(models.Model):
    from apps.users.models import MyUser
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name
