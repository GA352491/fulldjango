from django.contrib import admin
from django.urls import path
from sample import views

urlpatterns = [
    path('', views.home, name='home'),
]