"""
def create_presence(account_name='Guest'):
    '''
    Функция генерирует запрос о присутствии клиента
    :param account_name:
    :return:
    '''
    # {'action': 'presence', 'time': 1573760672.167031, 'user': {'account_name': 'Guest'}}
    out = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: account_name
        }
    }
    return out

def process_ans(message):
    '''
    Функция разбирает ответ сервера
    :param message:
    :return:
    '''
    if RESPONSE in message:  # {RESPONSE: 200} / {RESPONSE: 400, ERROR: 'Bad Request'}
        if message[RESPONSE] == 200:
            return '200 : OK'
        return f'400 : {message[ERROR]}'
    raise ValueError
"""
import unittest
from client import *


class TestClient(unittest.TestCase):

    def test_presence_ACTION_contain(self):
        # Ошибка, если ключа 'action' нет в словаре
        self.assertTrue(ACTION in create_presence().keys())

    def test_presence_ACTION_value(self):
        # Ошибка, если значение ключа 'action' != 'presence'
        self.assertEqual(create_presence().setdefault(ACTION), PRESENCE)

    def test_presence_TIME_contain(self):
        # Ошибка, если ключа 'time' нет в словаре
        self.assertTrue(TIME in create_presence().keys())  # (TIME = 'time')

    def test_presence_TIME_value(self):
        # Ошибка, если значение ключа 'time' != вещественным число (float)
        self.assertEqual(type(create_presence().setdefault(TIME)), float)

    def test_presence_USER_contain(self):
        # Ошибка, если ключа 'user' нет в словаре
        self.assertTrue(USER in create_presence().keys())

    def test_presence_NAME_contain_in_USER(self):
        # Ошибка, если ключа 'account_name' нет в значении ключа 'user' {... 'user': {'account_name': 'Guest'}}
        self.assertTrue(ACCOUNT_NAME in list(create_presence().items())[-1][-1].keys())  # dict_keys(['account_name'])

    def test_presence_NAME_value_in_USER(self):
        # В нашем случае ошибка, если имя пользователя != 'Guest'
        self.assertEqual(list(create_presence().items())[-1][-1].setdefault(ACCOUNT_NAME), 'Guest')

    """
    def process_ans(message):
    '''
    Функция разбирает ответ сервера
    :param message:
    :return:
    '''
    if RESPONSE in message:  # {RESPONSE: 200} / {RESPONSE: 400, ERROR: 'Bad Request'}
        if message[RESPONSE] == 200:
            return '200 : OK'
        return f'400 : {message[ERROR]}'
    raise ValueError
    """

    def test_process_ans_NAME_value_in_USER(self):
        pass


if __name__ == '__main__':
    main()

print(list(create_presence().items())[-1][-1].setdefault(ACCOUNT_NAME))
