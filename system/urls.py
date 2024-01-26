from django.urls import path
from .views import SystemAPIView

urlpatterns = [
    path('system', SystemAPIView.as_view(), name='system-list-create'),
    path('system/<int:id>', SystemAPIView.as_view(), name='system-retrieve-update'),
]
