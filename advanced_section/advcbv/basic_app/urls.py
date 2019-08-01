from . import views
from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path

app_name = 'basic_app'

urlpatterns = [
    url(r'^$', views.SchoolListView.as_view(), name='list'),
    url(r'^<int:pk>/', views.SchoolDetailView.as_view(), name='detail'),
    url(r'^create/', views.SchoolCreateView.as_view(), name='create'),
    url(r'^update/<int:pk>/', views.SchoolUpdateView.as_view(), name='update'),
    url(r'^delete/<int:pk>/', views.SchoolDeleteView.as_view(), name='delete')
]
