from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password-reset-sent/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_sent.html'), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_form.html'), name='password_reset_confirm'),
    path('password-reset-complete/',  auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
    path('profile_picture_uploader/', views.profile_picture_upload_view, name='profile_picture_uploader'),
    path('talent/<int:user_id>/', views.talent_profile_view, name='talent_profile'),

]
