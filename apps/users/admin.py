from django.contrib import admin
from .models import TalentAccount

from image_cropping import ImageCroppingMixin

class TalentAccountAdmin(ImageCroppingMixin, admin.ModelAdmin):
	pass

admin.site.register(TalentAccount, TalentAccountAdmin)
