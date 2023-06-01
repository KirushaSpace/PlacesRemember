from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('create_note/', views.create_note, name='create')
]