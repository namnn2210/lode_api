from django.urls import path
from .views import fetch_cities, fetch_games, fetch_rates, get_games, get_cities, get_rates, get_all_cities

urlpatterns = [
    path('city/fetch/', fetch_cities, name='fetch_cities'),
    path('game/fetch/', fetch_games, name='fetch_games'),
    path('rate/fetch/', fetch_rates, name='fetch_rates'),
    path('api/game/<str:region>/', get_games, name='get_games'),
    path('api/city/<str:region>/', get_cities, name='get_cities'),
    path('api/cities/', get_all_cities, name='get_all_cities'),
    path('api/rate/', get_rates, name='get_rates')
]
