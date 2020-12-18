"""Программа-сервер"""

import socket
import sys
import json
from common.variables import ACTION, ACCOUNT_NAME, RESPONSE, MAX_CONNECTIONS, \
    PRESENCE, TIME, USER, ERROR, DEFAULT_PORT
from common.utils import get_message, send_message
from log.configs.server_log_config import server_logger
from decorators import log

LOGGER = server_logger


@log
def process_client_message(message):
    '''
    Обработчик сообщений от клиентов, принимает словарь -
    сообщение от клинта, проверяет корректность,
    возвращает словарь-ответ для клиента

    :param message:
    :return:
    '''
    if ACTION in message and message[ACTION] == PRESENCE and TIME in message \
            and USER in message and message[USER][ACCOUNT_NAME] == 'Guest':
        LOGGER.debug('Отправлен положительный ответ на "Presence"-сообщение клиента: {RESPONSE: 200}')
        return {RESPONSE: 200}

    LOGGER.debug('Отправлен отрицательный ответ на "Presence"-сообщение клиента: {RESPONSE: 400, ERROR: "Bad Request"}')
    return {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }


def main_server():
    '''
    Загрузка параметров командной строки, если нет параметров, то задаём значения по умоланию.
    Сначала обрабатываем порт:
    server.py -p 8079 -a 192.168.1.2
    :return:
    '''

    try:
        if '-p' in sys.argv:
            listen_port = int(sys.argv[sys.argv.index('-p') + 1])
        else:
            listen_port = DEFAULT_PORT
        if listen_port < 1024 or listen_port > 65535:
            LOGGER.critical('Ошибка указания порта для соединения (порт не в диапазоне от 1024 до 65535)')
            raise ValueError
    except IndexError:
        LOGGER.critical('Ошибка обработки параметров командной строки: '
                        'после параметра -\'p\' необходимо указать номер порта.')
        # print('После параметра -\'p\' необходимо указать номер порта.')
        sys.exit(1)
    except ValueError:
        LOGGER.critical('Ошибка указания порта для соединения (порт не в диапазоне от 1024 до 65535)')
        # print('В качастве порта может быть указано только число в диапазоне от 1024 до 65535.')
        sys.exit(1)

    # Затем загружаем какой адрес слушать

    try:
        if '-a' in sys.argv:
            listen_address = sys.argv[sys.argv.index('-a') + 1]
        else:
            listen_address = ''

    except IndexError:
        LOGGER.critical('Ошибка обработки параметров командной строки: '
                        'после параметра \'a\'- необходимо указать адрес, который будет слушать сервер.')
        # print('После параметра \'a\'- необходимо указать адрес, который будет слушать сервер.')
        sys.exit(1)

    # Готовим сокет

    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.bind((listen_address, listen_port))

    # Слушаем порт

    transport.listen(MAX_CONNECTIONS)

    while True:
        client, client_address = transport.accept()
        try:
            message_from_cient = get_message(client)
            LOGGER.info(f'Принято "Presence"-сообщение от клиента: {list(message_from_cient.values())}')
            print(message_from_cient)
            # {'action': 'presence', 'time': 1573760672.167031, 'user': {'account_name': 'Guest'}}
            response = process_client_message(message_from_cient)
            send_message(client, response)
            # LOGGER.debug(f'Отправлено сообщение клиенту: {response}')
            client.close()
        except (ValueError, json.JSONDecodeError):
            LOGGER.error('Принято некорретное сообщение от клиента.')
            # print('Принято некорретное сообщение от клиента.')
            client.close()


if __name__ == '__main__':
    main_server()
