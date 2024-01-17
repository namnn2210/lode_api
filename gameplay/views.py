from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Order
# Create your views here.
import json


@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def save_order(request):
    body = json.loads(request.body.decode('utf-8'))
    order = Order(**body)
    order.save()
    return Response({
        "success": True,
        "rows": body,
        "attrs": []
    })
