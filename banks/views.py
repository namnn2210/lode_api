from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Bank
import requests


@api_view(['GET'])
@permission_classes([AllowAny])
def fetch_banks(request):
    response = requests.get('https://qr.sepay.vn/banks.json').json()['data']
    for data in response:
        print(data)
        bank = Bank(name=data['name'], code=data['code'], bin=data['bin'], short_name=data['short_name'])
        bank.save()
    return response
