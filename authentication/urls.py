from django.urls import path
from .views import signup, login, account

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('account/', account, name='account')
]
