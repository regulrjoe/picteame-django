from django.shortcuts import render, redirect

# Create your views here.

# ----------------------
def home_view(request):
    context = {}
    return render(request, 'app_main/home.html', context)

