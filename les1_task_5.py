"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import subprocess
import chardet


ya_args = ['ping', 'yandex.ru']
ya_ping = subprocess.Popen(ya_args, stdout=subprocess.PIPE)
you_args = ['ping', 'youtube.com']
you_ping = subprocess.Popen(you_args, stdout=subprocess.PIPE)

list_of_strings = ya_ping
l = 0
n = 0
while n < 2:
    if l == 6:
        list_of_strings = you_ping
        l = 0
    for line in list_of_strings.stdout:
        if l > 5:
            break
        result = chardet.detect(line)
        line = line.decode(result['encoding']).encode('utf-8')
        print(line.decode('utf-8'))
        l += 1
    n += 1

