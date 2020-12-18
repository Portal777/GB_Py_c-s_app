"""
Продолжая задачу логирования, реализовать декоратор @log, фиксирующий обращение к декорируемой функции.
Он сохраняет ее имя и аргументы.
2. В декораторе @log реализовать фиксацию функции, из которой была вызвана декорированная. Если имеется такой код:
@log
def func_z():
 pass

def main():
 func_z()
...в логе должна быть отражена информация:
"<дата-время> Функция func_z() вызвана из функции main"
"""
import traceback
import sys
import inspect
# from functools import wraps
from log.configs.client_log_config import client_logger
from log.configs.server_log_config import server_logger

if sys.argv[0].find('client') == -1:
    LOGGER = server_logger
else:
    LOGGER = client_logger


def log(func):  # декоратор
    def decorated(*args, **kwargs):  # обертка, дополняющая декарируемую функцию
        res = func(*args, **kwargs)
        LOGGER.debug(f'Была вызвана функция {func.__name__}, с параметрами: {args}, {kwargs}. '
                     f'Вызов был из модуля {func.__module__}. '
                     f'Вызывающая функция: {traceback.format_stack()[0].split()[-1]}', stacklevel=2)
        return res

    return decorated

# class Log():
#
#     def __init__(self):
#         pass
#
#     def __call__(self, func):
#         def decorated(*args, **kwargs):
#             res = func(*args, **kwargs)
#             LOGGER.debug(f'Была вызвана функция {func.__name__}, с параметрами: {args}, {kwargs}. '
#                          f'Вызов был из модуля {func.__module__}. '
#                          f'Вызывающая функция: {traceback.format_stack()[0].split()[-1]}', stacklevel=2)
#
#             return res
#
#         return decorated
