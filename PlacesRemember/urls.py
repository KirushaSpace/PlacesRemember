from django.contrib import admin
from django.urls import path, include
from ninja import NinjaAPI
from service.api import router

api = NinjaAPI()
api.add_router('/', router)

urlpatterns = [
    path('', include('service.urls')),
    path('admin/', admin.site.urls),
    path('api/', api.urls, name='api')
]
