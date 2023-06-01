from django.contrib import admin
from django.urls import path, include
from service.api import api

urlpatterns = [
    path('', include('service.urls')),
    path('admin/', admin.site.urls),
    path('api/', api.urls)
]
