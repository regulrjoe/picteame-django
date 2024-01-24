from django.db import models
from django_countries.fields import CountryField

# ------------------------
class City(models.Model):
    city = models.CharField('City', max_length=100)
    state = models.CharField('State', max_length=100)
    country = CountryField(default='MX')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.city  + ', ' + self.state + ' ' + self.country.code

# ------------------------
class Category(models.Model):
    name = models.CharField('Categoy name', max_length=100, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# ------------------------
class Fee(models.Model):
    title = models.CharField('Fee title', max_length=128, null=True)
    description = models.CharField('Fee description', max_length=1024, null=True)
    talent = models.ForeignKey('users.TalentAccount', on_delete=models.SET_NULL, null=True)
    categories = models.ManyToManyField(Category)
    price_per_hour = models.FloatField()
    photos_per_hour = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.title:
            return self.title
        else:
            title = ''
            for c in categories.all:
                title += c + ' '
            return title + ' Fee'

# ------------------------
class Photo(models.Model):
    image = models.ImageField(blank=False, null=True)
    talent = models.ForeignKey('users.TalentAccount', on_delete=models.CASCADE, null=True)
    categories = models.ManyToManyField(Category)

    created_at = models.DateTimeField(auto_now_add=True)
