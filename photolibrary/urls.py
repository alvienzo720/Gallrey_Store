from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.loginUser, name="login"),
    path('register/', views.registerUser, name="register"),
    path('home/', views.home, name='home'),
    path('photo/<str:pk>/', views.expandImage, name='photo'),
    path('createPhoto/', views.createPhoto, name='createPhoto'),
    path('logout/', views.logoutUser, name="logout"),


   

    ]