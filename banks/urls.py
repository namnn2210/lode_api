from django.urls import path
from .views import fetch_banks, BankView

urlpatterns = [
    path('fetch', fetch_banks, name='fetch_banks'),
    path('banks', BankView.as_view(), name='banks'),
]
