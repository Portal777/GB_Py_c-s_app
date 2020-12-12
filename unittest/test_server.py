import unittest
from server import *  # в том числе и все в variables

""" if ACTION in message and message[ACTION] == PRESENCE and TIME in message \
            and USER in message and message[USER][ACCOUNT_NAME] == 'Guest':
        return {RESPONSE: 200}
    return {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }
    
{ACTION: 'presence', TIME: 1573760672.167031, USER: {ACCOUNT_NAME: 'Guest'}}
'user': {'account_name': 'Guest'}
"""


class TestServer(unittest.TestCase):

    def setUp(self):
        self.correct = {RESPONSE: 200}
        self.incorrect = {RESPONSE: 400, ERROR: 'Bad Request'}

    def testkey_Action_missing(self):
        # В нашем случае ошибка, если ACTION != 'presence'
        self.assertEqual(process_client_message(
            {TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}}), self.incorrect)

    def testkey_Action_wrong(self):
        # В нашем случае ошибка, если ACTION != 'presence'
        self.assertEqual(process_client_message(
            {ACTION: 'wrong', TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}}), self.incorrect)

    def testkey_TIME_missing(self):
        # Ошибка, если в сообщении не передавалось время (TIME)
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, USER: {ACCOUNT_NAME: 'Guest'}}), self.incorrect)

    def testkey_USER_missing(self):
        # Ошибка, если не передали пользователя (USER)
        self.assertEqual(process_client_message(
            {ACTION: 'presence', TIME: 1573760672.167031}), self.incorrect)

    def testkey_USER_wrong(self):
        # Ошибка, если имя пользователя != 'Guest'
        self.assertEqual(process_client_message(
            {ACTION: 'presence', TIME: 1573760672.167031, USER: {ACCOUNT_NAME: 'some user'}}), self.incorrect)


if __name__ == '__main__':
    main()
