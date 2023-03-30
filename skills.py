import os
import webbrowser
import sys
import subprocess

import voice

try:
    import requests
except:
    pass


def browser():

    webbrowser.open('https://www.yandex.com', new=2)


def game():
    try:
        subprocess.Popen('D:\Gang Beasts v1.3\Gang Beasts.exe')
    except:
        voice.speaker('Путь к файлу не найден, проверьте, правильный ли он')


def offpc():
    os.system('shutdown \s')
   # print('пк был бы выключен, но команде # в коде мешает;)))')


def weather():
    try:
        params = {'q': 'Moscow', 'units': 'metric', 'lang': 'ru', 'appid': 'ea421627d0291e90327e38c9d6321df1'}
        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather', params=params)
        if not response:
            raise
        w = response.json()
        voice.speaker(f"На улице {w['weather'][0]['description']} {round(w['main']['temp'])} градусов")

    except:
        voice.speaker('Произошла ошибка при попытке запроса к ресурсу API, проверь код')


def offBot():
    sys.exit()


def passive():
    pass