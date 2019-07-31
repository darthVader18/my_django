from django.urls import path
from second_app import views

urlpatterns = [
    path('', views.index, name="index"),
    path('users/', views.users, name="users"),
    path('help/', views.help, name='help'),
]
