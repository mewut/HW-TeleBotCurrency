import requests

import os


def form_query(query_format: str, base_url: str, access_key, query: str):
    return query_format.format(
        base_url=base_url,
        access_key=access_key,
        query=query,
    )


def get_currency_exchange_rate(currency: str, conversion_currency: str):
    access_key = os.environ['access_key']
    BASE_URL = 'https://www.exchangerate-api.com/'
    query = '{period}/{currency}'
    query_format = '{base_url}/{access_key}/{query}'
    query = query.format(
        period='latest',
        currency=currency,
    )

    query_url = form_query(
        query_format=query_format,
        base_url=BASE_URL,
        access_key=access_key,
        query=query,
    )
    response = requests.get(query_url)
    json_data = response.json()
    return json_data['conversion_rates'][conversion_currency]


# def main():
#     currency = input('Введите валюту:\t')
#     conversion_currency = input('Введите валюту для конвертирования:\t')
#     result = get_currency_exchange_rate(
#         currency=currency,
#         conversion_currency=conversion_currency,
#     )
#
#     print(f'{currency} в валюте {conversion_currency} стоит {result}')


# if __name__ == '__main__':
#     main()
