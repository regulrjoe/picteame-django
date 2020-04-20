from django.shortcuts import render, redirect
from apps.users.models import UserAccount

# Create your views here.

# ----------------------
def home_view(request):
    context = {}
    users = UserAccount.objects.all()
    context['users'] = users
    return render(request, 'core/home.html', context)

