from django.urls import path
from .views import get_user_statistical, get_statistical_by_date

urlpatterns = [
    path('user', get_user_statistical, name='statistical'),
    path('aggregate', get_statistical_by_date, name='aggregate')
]