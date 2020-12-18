"""
2. В каждом модуле выполнить настройку соответствующего логгера по следующему алгоритму:
Создание именованного логгера;
Сообщения лога должны иметь следующий формат: "<дата-время> <уровеньважности> <имямодуля> <сообщение>";
Журналирование должно производиться в лог-файл;
На стороне сервера необходимо настроить ежедневную ротацию лог-файлов.

3. Реализовать применение созданных логгеров для решения двух задач:
Журналирование обработки исключений try/except. Вместо функции print() использовать журналирование и обеспечить вывод
служебных сообщений в лог-файл;
Журналирование функций, исполняемых на серверной и клиентской сторонах при работе мессенджера.
"""
import logging.handlers
from common.variables import LOG_LEVEL

# создали регистратор и настроили уровень
server_logger = logging.getLogger('server_logger')
server_logger.setLevel(LOG_LEVEL)

if __name__ == '__main__':
    file_path = '../logs/server.log'
else:
    file_path = 'log/logs/server.log'

# создали файловый обработчик, для записи в файл
server_handler = logging.handlers.TimedRotatingFileHandler(file_path, encoding='utf-8', interval=1, when='D')

# создали переменную с форматом вывода сообщений для файлового обработчика
handler_format = logging.Formatter('%(asctime)s %(levelname)s %(filename)s %(message)s')

# применили форматирование к обработчику
server_handler.setFormatter(handler_format)

# подключили обработчик к регистратору
server_logger.addHandler(server_handler)

if __name__ == '__main__':
    server_logger.info('Тестовый запуск логирования')
