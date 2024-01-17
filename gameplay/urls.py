from django.urls import path
from .views import save_order, get_orders

urlpatterns = [
    path('save', save_order, name='save_order'),
    path('fetch', get_orders,name='get_orders')
]