"""
Задание 4.

Преобразовать слова 'разработка', 'администрирование', 'protocol',
'standard' из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

words = ['разработка', 'администрирование', 'protocol', 'standard']

c = 0
while c < 2:
    for i, x in enumerate(words):
        if c < 1:
            words[i] = x.encode('utf-8')
        else:
            words[i] = x.decode('utf-8')
    print(words)
    c += 1

