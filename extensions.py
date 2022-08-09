import json
import requests
from config import exchanges


class ApiException(Exception):
    pass


class Converter:
    @staticmethod
    def get_price(currency, conversion_currency, amount):
        try:
            currency = exchanges[currency.lower()]
        except KeyError:
            raise ApiException(f'Валюта {conversion_currency} не найдена!')
        try:
            currency = exchanges[currency.lower()]
        except KeyError:
            raise ApiException(f'Валюта {currency} не найдена!')

        if currency == conversion_currency:
            raise ApiException(f'Невозможно перевести одинаковые валюты {currency}!')

        try:
            amount = float(amount.replace(',', '.'))
        except ValueError:
            raise ApiException(f'Не удалось обработать количество {amount}!')

        r = requests.get(f'https://www.exchangerate-api.com/{access_key}latest?base={currency}&symbols={conversion_currency}')
        resp = json.loads(r.content)
        new_price = resp['rates'][conversion_currency] * float(amount)
        message = f'{currency} в валюте {conversion_currency} стоит {amount}'
        return message
