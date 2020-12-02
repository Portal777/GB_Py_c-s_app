"""
2. Задание на закрепление знаний по модулю json. Есть файл orders
в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий
его заполнение данными.

Для этого:
Создать функцию write_order_to_json(), в которую передается
5 параметров — товар (item), количество (quantity), цена (price),
покупатель (buyer), дата (date). Функция должна предусматривать запись
данных в виде словаря в файл orders.json. При записи данных указать
величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json()
с передачей в нее значений каждого параметра.

ПРОШУ ВАС НЕ УДАЛЯТЬ ИСХОДНЫЙ JSON-ФАЙЛ
ПРИМЕР ТОГО, ЧТО ДОЛЖНО ПОЛУЧИТЬСЯ

{
    "orders": [
        {
            "item": "printer",
            "quantity": "10",
            "price": "6700",
            "buyer": "Ivanov I.I.",
            "date": "24.09.2017"
        },
        {
            "item": "scaner",
            "quantity": "20",
            "price": "10000",
            "buyer": "Petrov P.P.",
            "date": "11.01.2018"
        }
    ]
}

вам нужно подгрузить JSON-объект
и достучаться до списка, который и нужно пополнять
а потом сохранять все в файл
"""

import json
from pathlib import Path


def write_to_json(item, quantity, price, buyer, data):
    with open('orders.json', 'r+') as f_n:
        objs = json.load(f_n)

        for i in objs.values():
            for x in i:
                keys_in_orders = list(x.keys())

    dict_to_json = {k: v for k, v in zip(keys_in_orders, [item, quantity, price, buyer, data])}

    # спасибо гуглу, код ниже записывает весь json в переменную data
    # добавляем в конец нашего списка необходимые строки и перезаписываем полностью весь файл orders.json
    path = Path('orders.json')
    data = json.loads(path.read_text(encoding='utf-8'))
    data['orders'].append(dict_to_json)
    path.write_text(json.dumps(data, indent=4), encoding='utf-8')


write_to_json('Xerox', 1, 10000, 'Penkov D.E.', '11.01.20')
write_to_json('Monitor', 3, 99000, 'God I.L.', '01.01.01')
write_to_json('Video card', 1, 100500, 'Nal G.N.', '20.12.20')
