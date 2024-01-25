from django.shortcuts import render, redirect
from apps.users.models import TalentAccount
from django.db import models
from django.contrib.auth.models import User

# Create your views here.

# ----------------------
def home_view(request):
    query = request.GET.get('query')
    users = TalentAccount.objects.all().distinct()

    if query:
        users = users.filter(
            models.Q(city__city__icontains=query) |
            models.Q(categories__name__icontains=query) |
            models.Q(name__icontains=query)
        )
    
    users = users.exclude(is_superuser=True).exclude(is_staff=True)

    context = {'users': users, 'query': query}
    return render(request, 'core/home.html', context)

