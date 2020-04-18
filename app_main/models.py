from django.db import models
# Create your models here.

# ------------------------
class Category(models.Model):
    name = models.CharField('Categoy name', max_length=100, unique=True)

    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

# ------------------------
class Event(models.Model):
    from app_talent.models import Talent
    talent = models.ForeignKey(Talent, on_delete=models.SET_NULL, null=True)

    from app_customer.models import Customer
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)

    categories = models.ManyToManyField(Category)
    date_time = models.DateTimeField(null=True)
    duration_hours = models.FloatField(null=True)
    total_cost = models.FloatField(null=True)
    address = models.OneToOneField(Address, on_delete=models.SET_NULL, null=True)

    date_created = models.DateTimeField(auto_now_add=True, null=True)

# ------------------------
class Photo(models.Model):
    from app_talent.models import Talent
    talent = models.ForeignKey(Talent, on_delete=models.SET_NULL, null=True)

    from app_customer.models import Customer
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)

    image = models.ImageField(blank=False, null=True)
    categories = models.ManyToManyField(Category)
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True)

    date_created = models.DateTimeField(auto_now_add=True, null=True)
