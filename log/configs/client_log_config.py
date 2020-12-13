import logging
from common.variables import LOG_LEVEL

# создали регистратор и настроили уровень
client_logger = logging.getLogger('client_logger')
client_logger.setLevel(LOG_LEVEL)

if __name__ == '__main__':
    file_path = '../logs/client.log'
else:
    file_path = 'log/logs/client.log'

# создали файловый обработчик, для записи в файл
client_handler = logging.FileHandler(file_path, encoding='utf-8')

# создали переменную с форматом вывода сообщений для файлового обработчика
handler_format = logging.Formatter('%(asctime)s %(levelname)s %(filename)s %(message)s')

# применили форматирование к обработчику
client_handler.setFormatter(handler_format)

# подключили обработчик к регистратору
client_logger.addHandler(client_handler)

if __name__ == '__main__':
    client_logger.info('Тестовый запуск логирования')
