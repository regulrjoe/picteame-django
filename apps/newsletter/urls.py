from django.urls import path
from . import views

urlpatterns = [
    path('subscribe/', views.subscribe_view, name='newsletter_subscribe'),
    path('confirm/', views.confirm_view, name='newsletter_confirm'),
    path('unsubscribe/', views.unsubscribe_view, name='newsletter_unsubscribe'),
]
