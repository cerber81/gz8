from datetime import datetime
from time import time


def start_app():
    time_calc = datetime.now().strftime('%H:%M')
    with open('log.csv', 'a') as log_file:
        log_file.write(f'"Start work with app" Time {time_calc}\n')


def error_enter():
    time_calc = datetime.now().strftime('%H:%M')
    with open('log.csv', 'a', encoding='utf-8') as log_file:
        log_file.write(f'{"Enter error"} Time {time_calc}\n')


