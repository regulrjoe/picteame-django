from django.db import models
from django_countries.fields import CountryField
from cities_light.models import City

# ------------------------
class ProxyCity(City):
    class Meta:
        proxy = True
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.name + ", " + self.region.name

# ------------------------
class Category(models.Model):
    name = models.CharField('Categoy name', max_length=100, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

# ------------------------
class Fee(models.Model):
    price = models.FloatField(null=False)
    title = models.CharField('Fee title', max_length=128, null=False)
    description = models.CharField('Fee description', max_length=1024, null=True)
    talent = models.ForeignKey('users.TalentAccount', on_delete=models.CASCADE, null=False)
    categories = models.ManyToManyField(Category)

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
