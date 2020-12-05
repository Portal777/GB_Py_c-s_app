"""
клиент отправляет запрос серверу;
сервер отвечает соответствующим кодом результата. Клиент и сервер должны быть реализованы в виде отдельных скриптов,
содержащих соответствующие функции.

Функции клиента: сформировать presence-сообщение; отправить сообщение серверу;
получить ответ сервера; разобрать сообщение сервера; параметры командной строки скрипта
client.py <addr> [<port>]: addr — ip-адрес сервера; port — tcp-порт на сервере, по умолчанию 7777.

Функции сервера: принимает сообщение клиента; формирует ответ клиенту; отправляет ответ клиенту;
имеет параметры командной строки: -p <port> — TCP-порт для работы (по умолчанию использует 7777); -a <addr> — IP-адрес
для прослушивания (по умолчанию слушает все доступные адреса).
"""
from variables import *
import json
import time


def send_message_to_server(account_name='Guest'):
    """Отправляем сообщение на сервер"""
    message = {
        "action": "presence",
        "time": time.ctime(time.time()),
        "user": {
            "account_name": account_name
        }
    }

    message_to_server = json.dumps(message).encode(ENCODING)
    return message_to_server  # передаём в функцию main(), в ней передаем в send_message в utils.py


def response_from_server(message_from_server):
    """Получили ответ с сервера (словарь: {response: код, alert/error: 'str') (через функцию get_message в utils.py)"""

    if RESPONSE in message_from_server:  # RESPONSE из variables.py
        if message_from_server[RESPONSE] == 200:
            return '200 : OK'
        return f'400 : {message_from_server[ERROR]}'
    raise ValueError
