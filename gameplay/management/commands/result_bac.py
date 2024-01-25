from django.core.management.base import BaseCommand, CommandError
from datetime import datetime
from server.models import City
from django.db.models import Q
import requests


class Command(BaseCommand):
    help = "Get result for region bac"

    def handle(self, *args, **options):
        current_datetime = datetime.now()
        print('now', current_datetime)
        weekday = current_datetime.weekday()
        print('weekday', weekday)
        current_date = current_datetime.date()
        print('current_date', current_date)
        # get cities equal weekday
        cities = City.objects.filter((Q(date__contains=str(weekday)) | Q(date='')) & Q(region='bac'))
        for city in cities:
            # Get result for cities
            data = {
                'date': current_date.strftime('%d-%m-%Y'),
                'city': city.result_domain
            }
            result = requests.get('http://localhost:8000/api/result', params=data).json()
            if result['data'] is not None:
                result_dict = result['data']['result']
                list_values = list(result_dict.values())
                for value in list_values:
                    if value != '':
                        list_numbers = [number.strip()[:-2] for number in value.split('-')]
                        print(list_numbers)
            # Get orders with order_date, city_id,
