from django.core.management.base import BaseCommand, CommandError
from datetime import datetime
from server.models import City
from gameplay.models import Order
from authentication.models import UserProfile
from django.db.models import Q
import requests


def format_result_dict(result_dict, prize='all'):
    print('bbbbbbbbbbbbbbbbbbbbbbbb', result_dict)
    result_list = []
    if prize == 'all':
        list_values = list(result_dict.values())
    else:
        list_values = result_dict[prize]
    # Remove hyphens from each string in the list
    for value in list_values:
        result_list += [x.strip() for x in value.split('-')]

    return result_list


def process_result(result_dict, order_numbers, order_mode):
    print(result_dict, order_numbers, order_mode)
    win = False
    total_number_won = 0
    if order_mode.type == 'loto':
        win, total_number_won = loto(result_dict, order_numbers, order_mode)
    elif order_mode.type == 'loxien':
        win, total_number_won = loxien(result_dict, order_numbers, order_mode)
    elif order_mode.type == 'dauduoi':
        win, total_number_won = dauduoi(result_dict, order_numbers, order_mode)
    elif order_mode.type == 'de':
        win, total_number_won = de(result_dict, order_numbers, order_mode)
    elif order_mode.type == '3cang':
        win, total_number_won = bacang(result_dict, order_numbers, order_mode)
    elif order_mode.type == 'loda':
        win, total_number_won = loda(result_dict, order_numbers, order_mode)
    elif order_mode.type == 'xiuchu':
        win, total_number_won = xiuchu(result_dict, order_numbers, order_mode)

    return win, total_number_won


def loto(result_dict, order_numbers, order_mode):
    result_list = format_result_dict(result_dict)
    print('==================== formated result list', result_list)
    number = 2
    if order_mode.code == 'loto_2so':
        number = 2
    if order_mode.code == 'loto_3so':
        number = 3
    print('game mode: ', order_mode.code)
    data_list = [item[-number:] for item in result_list if item and len(item) >= number]
    print('result list to compare', data_list)
    win, total_number_won = False, 0
    for number in order_numbers:
        existed = data_list.count(number)
        if existed > 0:
            total_number_won += existed
        else:
            print('number {} not won in list {}'.format(number, data_list))
    if total_number_won != 0:
        win = True
        return win, total_number_won
    else:
        return win, total_number_won


def loxien(result_dict, order_numbers, order_mode):
    print('lo xien', result_dict)
    result_list = format_result_dict(result_dict)
    number = 2
    if order_mode.code == 'loxien_2so':
        number = 2
    if order_mode.code == 'loxien_3so':
        number = 3
    if order_mode.code == 'loxien_4so':
        number = 4
    data_list = [item[-number:] for item in result_list if item and len(item) >= number]
    both_present = all(item in data_list for item in order_numbers)
    if both_present:
        return True, 1
    return False, 0


def dauduoi(result_dict, order_numbers, order_mode):
    result_list = format_result_dict(result_dict, prize='special')
    special = result_list[0]
    print('specialllllllll', special)
    check_number = ''
    if order_mode.code == 'dauduoi_dau':
        check_number = str(special[-2]).zfill(2)
    if order_mode.code == 'dauduoi_duoi':
        check_number = str(special[-1]).zfill(2)
    if check_number in order_numbers:
        return True, 1
    return False, 0


def de(result_dict, order_numbers, order_mode):
    win, total_number_won = False, 0
    if order_mode.code == 'de_dau':
        print('game mode: ', order_mode.code)
        result_list = format_result_dict(result_dict, prize='prize7')
        number = 2
        data_list = [item[-number:] for item in result_list if item and len(item) >= number]
        print('result list to compare', data_list)
        for number in order_numbers:
            existed = data_list.count(number)
            if existed > 0:
                total_number_won += existed
            else:
                print('number {} not won in list {}'.format(number, data_list))
        if total_number_won != 0:
            win = True
            return win, total_number_won
        else:
            return win, total_number_won
    if order_mode.code == 'de_dacbiet':
        print('game mode: ', order_mode.code)
        result_list = format_result_dict(result_dict, prize='special')
        number = 2
        data_list = [item[-number:] for item in result_list if item and len(item) >= number]
        for number in order_numbers:
            existed = data_list.count(number)
            if existed > 0:
                total_number_won += existed
            else:
                print('number {} not won in list {}'.format(number, data_list))
        if total_number_won != 0:
            win = True
            return win, total_number_won
        else:
            return win, total_number_won
    return False, 0


def bacang(result_dict, order_numbers, order_mode):
    win, total_number_won = False, 0
    if order_mode.code == '3cang' or order_mode.code == 'xiuchu_duoi':
        print('game mode: ', order_mode.code)
        result_list = format_result_dict(result_dict, prize='special')
        number = 3
        data_list = [item[-number:] for item in result_list if item and len(item) >= number]
        for number in order_numbers:
            existed = data_list.count(number)
            if existed > 0:
                total_number_won += existed
            else:
                print('number {} not won in list {}'.format(number, data_list))
        if total_number_won != 0:
            win = True
            return win, total_number_won
        else:
            return win, total_number_won
    if order_mode.code == 'xiuchu_dau':
        print('game mode: ', order_mode.code)
        result_list = format_result_dict(result_dict, prize='prize7')
        number = 3
        data_list = [item[-number:] for item in result_list if item and len(item) >= number]
        for number in order_numbers:
            existed = data_list.count(number)
            if existed > 0:
                total_number_won += existed
            else:
                print('number {} not won in list {}'.format(number, data_list))
        if total_number_won != 0:
            win = True
            return win, total_number_won
        else:
            return win, total_number_won
    if order_mode.code == 'xiuchu_dauduoi':
        print('game mode: ', order_mode.code)
        result_list = format_result_dict(result_dict, prize='special') + format_result_dict(result_dict, prize='prize7')
        number = 3
        data_list = [item[-number:] for item in result_list if item and len(item) >= number]
        for number in order_numbers:
            existed = data_list.count(number)
            if existed > 0:
                total_number_won += existed
            else:
                print('number {} not won in list {}'.format(number, data_list))
        if total_number_won != 0:
            win = True
            return win, total_number_won
        else:
            return win, total_number_won
    return False, 0


def loda(result_dict, order_numbers, order_mode):
    result_list = format_result_dict(result_dict)
    number = 2
    if order_mode.code == 'da_2so':
        number = 2
    if order_mode.code == 'da_3so':
        number = 3
    if order_mode.code == 'da_4so':
        number = 4
    data_list = [item[-number:] for item in result_list if item and len(item) >= number]
    both_present = all(item in data_list for item in order_numbers)
    if both_present:
        return True, 1
    return False, 0


def xiuchu(result_dict, order_numbers, order_mode):
    win, total_number_won = False, 0
    if order_mode.code == 'xiuchu_duoi':
        print('game mode: ', order_mode.code)
        result_list = format_result_dict(result_dict, prize='special')
        number = 3
        data_list = [item[-number:] for item in result_list if item and len(item) >= number]
        for number in order_numbers:
            existed = data_list.count(number)
            if existed > 0:
                total_number_won += existed
            else:
                print('number {} not won in list {}'.format(number, data_list))
        if total_number_won != 0:
            win = True
            return win, total_number_won
        else:
            return win, total_number_won
    if order_mode.code == 'xiuchu_dau':
        print('game mode: ', order_mode.code)
        result_list = format_result_dict(result_dict, prize='prize7')
        number = 3
        data_list = [item[-number:] for item in result_list if item and len(item) >= number]
        for number in order_numbers:
            existed = data_list.count(number)
            if existed > 0:
                total_number_won += existed
            else:
                print('number {} not won in list {}'.format(number, data_list))
        if total_number_won != 0:
            win = True
            return win, total_number_won
        else:
            return win, total_number_won
    if order_mode.code == 'xiuchu_dauduoi':
        print('game mode: ', order_mode.code)
        result_list = format_result_dict(result_dict, prize='special') + format_result_dict(result_dict, prize='prize7')
        number = 3
        data_list = [item[-number:] for item in result_list if item and len(item) >= number]
        for number in order_numbers:
            existed = data_list.count(number)
            if existed > 0:
                total_number_won += existed
            else:
                print('number {} not won in list {}'.format(number, data_list))
        if total_number_won != 0:
            win = True
            return win, total_number_won
        else:
            return win, total_number_won
    return False, 0


class Command(BaseCommand):
    help = "Lấy kết quả XS và tính thắng thua"

    def add_arguments(self, parser):
        parser.add_argument('-r', '--region', type=str, required=True, help='Region parameter')

    def handle(self, *args, **options):
        region = options["region"]
        print('Get result for region: ', options['region'])
        if region is not None:
            # Get cities by weekday + region
            # Loop cities -> get result of city -> loop orders by order_date city_id -> call func (city_result, order_number, mode_id)
            # Get result of order and get data return -> update order status and update user balance
            current_datetime = datetime.now()
            print('now', current_datetime)
            weekday = current_datetime.isoweekday()
            print('weekday', weekday)
            current_date = current_datetime.date()
            print('current_date', current_date)
            current_date_str = current_date.strftime("%Y-%m-%d")
            # current_date_str = '2024-01-23'

            # get cities equal weekday
            cities = City.objects.filter((Q(date__contains=str(weekday)) | Q(date='')) & Q(region=region))
            for city in cities:
                # Get result for cities
                data = {
                    'date': current_date.strftime('%d-%m-%Y'),
                    'city': city.result_domain
                }
                result = requests.get('http://localhost:8000/api/result', params=data).json()
                result_dict = {}
                if result['data'] is not None:
                    result_dict = result['data']['result']

                # Get orders with order_date, city_id,
                orders = Order.objects.filter(Q(order_date=current_date_str) & Q(city=city) & Q(status=False))
                for order in orders:
                    win, total_number_won = process_result(result_dict, order.numbers, order.mode)
                    print(win, total_number_won)
                    # Update order status and balance

                    if win:
                        order.status = True
                        order.win = True
                        order.save()

                        user_profile = UserProfile.objects.get(user=order.user)
                        user_profile.balance += order.bet_amount * order.mode.rate * total_number_won
                        print('user {} has won {}'.format(user_profile.phone, order.pay_number * total_number_won))
                        user_profile.save()
                    else:
                        order.status = True
                        order.win = False
                        order.total = True
                        order.save()
        else:
            raise CommandError('Error: the --region parameter is required.')
