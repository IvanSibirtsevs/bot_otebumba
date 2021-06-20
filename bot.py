
from random import randint, choice
from requests import get
from bs4 import BeautifulSoup
from threading import Timer
import telebot


token = '1731336324:AAGxbwM8Sz1XuK1YvEMSCTfTTM5CzDhYJ6w'
CHANNEL_NAME = '233431659'
bot = telebot.TeleBot(token)
bot.config['1731336324:AAGxbwM8Sz1XuK1YvEMSCTfTTM5CzDhYJ6w'] = token
bot.config['api_key'] = token


def send_compliment():
    Timer(2.0, send_compliment).start()
    bot.send_message(233431659, get_random_zalupa())

def  get_random_zalupa():
    random_page_number = str(randint(1, 42))
    webpage = get('http://kompli.me/komplimenty-devushke/page/' + random_page_number).text

    tags = BeautifulSoup(webpage, 'html.parser').\
        find_all('a')
    complements = []
    for tag in tags:
        tag_text = tag.get_text()
        if tag_text == 'Назад':
            break
        complements.append(tag_text)

    return choice(complements[4:])

send_compliment()
print(send_compliment())
