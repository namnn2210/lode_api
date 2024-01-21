from django.urls import path
from .views import fetch_banks

urlpatterns = [
    path('fetch', fetch_banks, name='fetch_banks'),
]
