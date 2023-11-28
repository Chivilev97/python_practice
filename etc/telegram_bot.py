from os import environ
import requests
import datetime as dt
import translate

CHAT_ID = environ['CHAT_ID']
BOT_TOKEN = environ['BOT_TOKEN']

translator = translate.Translator('ru')

response = requests.get(f'http://numbersapi.com/{dt.date.today().month}/{dt.date.today().day}/date').text
API_link = f'https://api.telegram.org/{BOT_TOKEN}'
get_message = requests.get(API_link + f'/sendMessage?chat_id={CHAT_ID}&text={translator.translate(response)}')
