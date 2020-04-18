from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(City)
admin.site.register(Category)
admin.site.register(Photo)
admin.site.register(Address)
admin.site.register(Event)
