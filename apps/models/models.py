from django.db import models
from django_countries.fields import CountryField

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
class CustomerProfile(models.Model):

    def __str__(self):
        return self.user.name

# ------------------------
class Category(models.Model):
    name = models.CharField('Categoy name', max_length=100, unique=True)

    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

# ------------------------
class TalentProfile(models.Model):
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.user.name

# ------------------------
class Fee(models.Model):
    title = models.CharField('Fee title', max_length=128, null=True)
    description = models.CharField('Fee description', max_length=1024, null=True)
    talent = models.ForeignKey(TalentProfile, on_delete=models.CASCADE)
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

# ------------------------
class Event(models.Model):
    talent = models.ForeignKey(TalentProfile, on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(CustomerProfile, on_delete=models.SET_NULL, null=True)
    categories = models.ManyToManyField(Category)

    date_time = models.DateTimeField(null=True)
    duration_hours = models.FloatField(null=True)
    total_cost = models.FloatField(null=True)
    address = models.OneToOneField(Address, on_delete=models.SET_NULL, null=True)

    date_created = models.DateTimeField(auto_now_add=True, null=True)

# ------------------------
class Photo(models.Model):
    image = models.ImageField(blank=False, null=True)

    talent = models.ForeignKey(TalentProfile, on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(CustomerProfile, on_delete=models.SET_NULL, null=True)

    categories = models.ManyToManyField(Category)
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True)

    date_created = models.DateTimeField(auto_now_add=True, null=True)
