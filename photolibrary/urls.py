from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    
    path('', views.loginUser, name="login"),
    path('register/', views.registerUser, name="register"),
    path('home/', views.home, name='home'),
    path('photo/<str:pk>/', views.expandImage, name='photo'),
    path('createPhoto/', views.createPhoto, name='createPhoto'),
    path('logout/', views.logoutUser, name="logout"),


    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='photolibrary/password_reset.html'), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='photolibrary/password_reset_sent.html'), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='photolibrary/password_reset_form.html'), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='photolibrary/password_reset_done.html'), name="password_reset_complete"),







    ]