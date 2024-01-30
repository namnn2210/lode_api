from django.urls import path, include
from .views import signup, login, account, PasswordResetView, PasswordResetConfirmView, password_change

urlpatterns = [
    path('signup', signup, name='signup'),
    path('login', login, name='login'),
    path('account', account, name='account'),
    path('password-reset', PasswordResetView.as_view(), name='password-reset'),
    path('password-reset/confirm/<str:uidb64>/<str:token>', PasswordResetConfirmView.as_view(),
         name='password-reset-confirm'),
    path('password-change', password_change,
         name='password-change'),
]
