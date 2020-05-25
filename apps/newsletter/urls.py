from django.urls import path
from . import views

urlpatterns = [
    path('talent/subscribe', views.subscribe_talent_view, name='newsletter_talent_subscribe'),
    path('confirm/', views.confirm_view, name='newsletter_confirm'),
    path('unsubscribe/', views.unsubscribe_view, name='newsletter_unsubscribe'),
]
