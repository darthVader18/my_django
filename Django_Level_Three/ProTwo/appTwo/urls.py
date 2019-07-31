from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('users/', views.users, name="users"),
    path('help/', views.help, name='help'),
]
