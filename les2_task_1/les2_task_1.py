"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт,
осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt,
info_3.txt и формирующий новый «отчетный» файл в формате CSV.

Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов
с данными, их открытие и считывание данных. В этой функции из считанных данных
необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список. Должно
получиться четыре списка — например, os_prod_list, os_name_list,
os_code_list, os_type_list. В этой же функции создать главный список
для хранения данных отчета — например, main_data — и поместить в него
названия столбцов отчета в виде списка: «Изготовитель системы»,
«Название ОС», «Код продукта», «Тип системы». Значения для этих
столбцов также оформить в виде списка и поместить в файл main_data
(также для каждого файла);
"""

import csv
import chardet
import re

file_list = ['info_1.txt', 'info_2.txt', 'info_3.txt']


def get_data():
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = [[]]

    for open_file in file_list:

        detect = open(open_file, 'rb').read()
        result = chardet.detect(detect)  # определили кодировку, ибо файл не отрабатывал нормально

        with open(open_file, encoding=result.get('encoding')) as f_o:
            f_o_reader = csv.reader(f_o)
            for row in f_o_reader:
                row = row[0]  # для нормального отображения в регулярных выражениях

                match_prod = re.search(r'Изготовитель системы', row)
                match_name = re.search(r'Название ОС', row)
                match_code = re.search(r'Код продукта', row)
                match_type = re.search(r'Тип системы', row)

                if match_prod is not None:  # проверяем не пустое ли значение поиска регулярки на текущей строке
                    os_prod_list.append(re.split(r'Изготовитель системы\S*\s*', row)[1])  # добавляем в общий список
                    if match_prod.group() not in main_data[0]:  # проверяем, нет ли значения строки в списке main_data
                        main_data[0].insert(0, match_prod.group())  # добавляем название значения в список main_data
                if match_name is not None:
                    os_name_list.append(re.split(r'Название ОС\S*\s*', row)[1])
                    if match_name.group() not in main_data[0]:
                        main_data[0].insert(1, match_name.group())
                if match_code is not None:
                    os_code_list.append(re.split(r'Код продукта\S*\s*', row)[1])
                    if match_code.group() not in main_data[0]:
                        main_data[0].insert(2, match_code.group())
                if match_type is not None:
                    os_type_list.append(re.split(r'Тип системы\S*\s*', row)[1])
                    if match_type.group() not in main_data[0]:
                        main_data[0].insert(3, match_type.group())

    # создаем список с кол-ом вложенных списков, равных длине списка с файлами, по которым проходимся.
    # будет представлять собой массив списков, в которые помещены итоговые данные по файлу
    result_data = [[k + 1] for k, v in enumerate(file_list)]

    for array in [os_prod_list, os_name_list, os_code_list, os_type_list]:
        for k, v in enumerate(array):
            result_data[k].append(v)

    for value in result_data:  # проходимся по списку выше и добавляем каждый список в итоговый массив
        main_data.append(value)

    return main_data


"""Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(),
а также сохранение подготовленных данных в соответствующий CSV-файл;
"""


def write_to_csv(file):
    with open(file, 'w') as f_w:
        f_w_writer = csv.writer(f_w)
        f_w_writer.writerows(get_data())


write_to_csv('new_data_report.csv')

"""
Пример того, что должно получиться:

Изготовитель системы,Название ОС,Код продукта,Тип системы

1,LENOVO,Windows 7,00971-OEM-1982661-00231,x64-based

2,ACER,Windows 10,00971-OEM-1982661-00231,x64-based

3,DELL,Windows 8.1,00971-OEM-1982661-00231,x86-based
"""
