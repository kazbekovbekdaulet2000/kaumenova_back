import requests
from django.conf import settings


def send_reminder(price, client_phone_number):
    api_key = settings.MOBIZONE_API_KEY
    phone_num = '77762256136'
    headers = {
        'cache-control': 'no-cache',
    }
    params = {
        'output': 'json',
        'api': 'v1',
        'apiKey': api_key,
    }
    data = {
        'recipient': phone_num,
        'text': f'AidaKaumenova, новый заказ на сумму {price} тг, номер клиента - {client_phone_number}',
    }
    requests.post('https://api.mobizon.kz/service/message/sendSmsMessage', params=params, headers=headers, data=data)
    
