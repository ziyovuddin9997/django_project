from django.urls import path

from app_main.views import products


urlpatterns = [
    path('', products),  # http://localhost:8000
]
