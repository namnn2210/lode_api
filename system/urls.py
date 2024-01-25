from django.urls import path
from .views import SystemModelListCreateView, SystemModelRetrieveUpdateView

urlpatterns = [
    path('system', SystemModelListCreateView.as_view(), name='system-list-create'),
    path('system/<int:system_id>', SystemModelRetrieveUpdateView.as_view(), name='system-retrieve-update'),
]
