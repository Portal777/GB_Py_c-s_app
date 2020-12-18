"""Программа-клиент"""

import sys
import json
import socket
import time
from common.variables import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, \
    RESPONSE, ERROR, DEFAULT_IP_ADDRESS, DEFAULT_PORT
from common.utils import get_message, send_message
from log.configs.client_log_config import client_logger
from decorators import log

LOGGER = client_logger


@log
def create_presence(account_name='Guest'):
    """
    Функция генерирует запрос о присутствии клиента
    :param account_name:
    :return:
    """
    # {'action': 'presence', 'time': 1573760672.167031, 'user': {'account_name': 'Guest'}}
    out = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: account_name
        }
    }
    LOGGER.info(f'Отправили "Presence"-сообщение на сервер')
    return out


@log
def process_ans(message):
    """
    Функция разбирает ответ сервера
    :param message:
    :return:
    """
    if RESPONSE in message:
        if message[RESPONSE] == 200:
            LOGGER.debug(f'Получили положительный ответ на "Presence"-сообщение: "200 : OK"')
            return '200 : OK'
        LOGGER.debug(f'Получили отрицательный ответ на "Presence"-сообщение: "400 : {message[ERROR]}"')
        return f'400 : {message[ERROR]}'
    LOGGER.error('Произошла ошибка при принятии ответа от сервера на "Presence"-сообщение')
    raise ValueError


def main_client():
    """Загружаем параметы коммандной строки"""
    # client.py 192.168.1.2 8079
    try:
        server_address = sys.argv[1]
        server_port = int(sys.argv[2])
        if server_port < 1024 or server_port > 65535:
            LOGGER.critical('В качестве порта может быть указано только число в диапазоне от 1024 до 65535.')
            raise ValueError
    except IndexError:
        LOGGER.debug(f'Установлены значения по умолчанию для адреса({DEFAULT_IP_ADDRESS}) и порта({DEFAULT_PORT})')
        server_address = DEFAULT_IP_ADDRESS
        server_port = DEFAULT_PORT
    except ValueError:
        LOGGER.critical('В качестве порта может быть указано только число в диапазоне от 1024 до 65535.')
        # print('В качестве порта может быть указано только число в диапазоне от 1024 до 65535.')
        sys.exit(1)

    # Инициализация сокета и обмен

    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.connect((server_address, server_port))
    message_to_server = create_presence()
    send_message(transport, message_to_server)
    try:
        answer = process_ans(get_message(transport))
        print(answer)
    except (ValueError, json.JSONDecodeError):
        LOGGER.critical('Не удалось декодировать сообщение сервера.')
        # print('Не удалось декодировать сообщение сервера.')


if __name__ == '__main__':
    main_client()
