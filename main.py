import telebot
from extensions import *
from config import *
import traceback

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу, введите данные в следующем формате: \n' \
           'название валюты - в какую валюту перевести - \n' \
           'количество переводимой валюты \n' \
           'Список доступных валют: /values'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in exchanges.keys():
        text = '\n' .join((text, key))
        bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def converter(message: telebot.types.Message):
    currency, conversion_currency, amount = message.text.split()
    new_price = Converter.get_price(currency, conversion_currency, amount)
    bot.reply_to(message, f'{currency} в валюте {conversion_currency} стоит {amount}')

@bot.message_handler(content_types=['text'])
def converter(message: telebot.types.Message):
    values = message.text.split(' ')
    try:
        if len(values) != 3:
            raise ApiException('Неверное количество параметров!')
        answer = Converter.get_price(*values)
    except ApiException as e:
        bot.reply_to(message, f'Ошибка в команде:\n{e}')
    except Exception as e:
        traceback.print_tb(e.__traceback__)
        bot.reply_to(message, f'Неизвестная ошибка:\n{e}')
    else:
        bot.reply_to(message, answer)

bot.polling()
