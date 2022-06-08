from django.contrib import admin
from django.urls import path, re_path, include
from . import views

# app_name = 'main'
urlpatterns = [
    
    path('', views.user_home, name='user_home'),
    path('DR/', views.drdetection, name= 'drdetection'),
    ]
