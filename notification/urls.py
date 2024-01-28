from django.urls import path
from .views import NotificationAPIView, NotificationCategoryAPIView, read_notifications

urlpatterns = [
    path('notification_category', NotificationCategoryAPIView.as_view(), name='notification_category'),
    path('notification_category/<int:cat_id>', NotificationCategoryAPIView.as_view(), name='notification_category-detail'),
    path('notification', NotificationAPIView.as_view(), name='notification'),
    path('notification/<int:notification_id>', NotificationAPIView.as_view(), name='notification-detail'),
    path('notification/read',read_notifications, name='read_notifications')
]
