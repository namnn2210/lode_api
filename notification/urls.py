from django.urls import path
from .views import NotificationAPIView, NotificationCategoryAPIView

urlpatterns = [
    path('notification_category', NotificationCategoryAPIView.as_view(), name='notification_category'),
    path('notification', NotificationAPIView.as_view(), name='notification'),
]
