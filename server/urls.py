from django.urls import path
from .views import fetch_games, fetch_rates, get_games, get_banking, get_rates, get_cities, get_result, deposit, \
    withdraw, get_user_profile_by_phone
from .views import SubgameAPIView, GameAPIView, UserAPIView, UserProfileAPIView, BalanceTransactionsAPIView, \
    BankingAPIView, NumbersView

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

    path('api/subgames', SubgameAPIView.as_view(), name='subgame-list'),
    path('api/subgames/<int:subgame_id>', SubgameAPIView.as_view(), name='subgame-detail'),

    path('api/games', GameAPIView.as_view(), name='game-list'),
    path('api/games/<int:game_id>', GameAPIView.as_view(), name='game-detail'),

    path('api/users', UserAPIView.as_view(), name='user-list'),
    path('api/users/<int:user_id>', UserAPIView.as_view(), name='user-detail'),

    path('api/users', UserAPIView.as_view(), name='user-list'),
    path('api/users/<int:user_id>', UserAPIView.as_view(), name='user-detail'),

    path('api/user_profiles', UserProfileAPIView.as_view(), name='user-profile-list'),
    path('api/user_profiles/<int:user_profile_id>', UserProfileAPIView.as_view(), name='user-profile-detail'),
    path('api/user_profiles/phone', get_user_profile_by_phone, name='user-profile-by-phone'),

    path('api/balance_transaction', BalanceTransactionsAPIView.as_view(), name='balance_transactions-list'),
    path('api/balance_transaction/<int:transaction_id>', BalanceTransactionsAPIView.as_view(),
         name='balance_transactions-detail'),

    path('api/banking', BankingAPIView.as_view(), name='banking-list'),
    path('api/banking/<int:banking_id>', BankingAPIView.as_view(), name='banking-detail'),

    path('api/count_total', NumbersView.as_view(), name='count_total')
]
