from django.db import models

# Create your models here.

# ------------------------
class Talent(models.Model):
    from apps.users.models import MyUser
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    from app_main.models import Category
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.user.name

# ------------------------
class Fee(models.Model):
    title = models.CharField('Fee title', max_length=128, null=True)
    description = models.CharField('Fee description', max_length=1024, null=True)
    talent = models.ForeignKey(Talent, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    price_per_hour = models.FloatField()
    photos_per_hour = models.IntegerField()

    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        if self.title:
            return self.title
        else:
            title = ''
            for c in categories.all:
                title += c + ' '
            return title + ' Fee'
