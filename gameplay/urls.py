from django.urls import path
from .views import save_order

urlpatterns = [
    path('save', save_order, name='save_order'),
]