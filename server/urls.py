from django.urls import path
from .views import fetch_games, fetch_rates, get_games, get_banking, get_rates, get_cities, get_result, deposit, \
    withdraw, get_balance_transactions
from .views import SubgameAPIView

urlpatterns = [
    path('game/fetch', fetch_games, name='fetch_games'),
    path('rate/fetch', fetch_rates, name='fetch_rates'),
    path('api/game/<str:region>', get_games, name='get_games'),
    path('api/cities', get_cities, name='get_cities'),
    path('api/result', get_result, name='get_result'),
    path('api/rate', get_rates, name='get_rates'),
    path('api/banking', get_banking, name='get_banking'),
    path('api/deposit', deposit, name='deposit'),
    path('api/withdraw', withdraw, name='withdraw'),
    path('api/balance_transaction', get_balance_transactions, name='get_balance_transactions'),

    path('api/subgame', SubgameAPIView.as_view(), name='subgame')
]
