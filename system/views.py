from django.shortcuts import render
from rest_framework import generics, permissions
from .models import SystemModel
from .serializer import SystemModelSerializer


# Create your views here.
class SystemModelListCreateView(generics.ListCreateAPIView):
    queryset = SystemModel.objects.all(status=True)
    serializer_class = SystemModelSerializer


class SystemModelRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = SystemModel.objects.all(status=True)
    serializer_class = SystemModelSerializer
    lookup_field = 'system_id'
