from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from . import views

# SET THE NAMESPACE!
app_name = 'basic_app'

urlpatterns = [
    url(r'^relative/$', views.relative, name='relative'),
    url(r'^other/$', views.other, name='other'),
]
