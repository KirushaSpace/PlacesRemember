from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('create_note/', views.create_note, name='create'),
    path('', include('social_django.urls')),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout')
]