import json


class Operation:
    all_operations = []

    def __init__(self, data):
        self.date = data.get('date')
        self.state = data.get('state')
        if data.get('operationAmount') != None:
            self.operationAmount = data.get('operationAmount').get('amount')
            self.nominal = data.get('operationAmount').get('currency').get('name')
        else:
            self.operationAmount = data.get('operationAmount')
        self.description = data.get('description')
        self.from_operation = data.get('from')
        self.to = data.get('to')

    def __str__(self):
        return f'{self.date} {self.description} {self.from_operation} {self.to} {self.operationAmount}'

    def __eq__(self, other):
        return self.date == other.date

    def __lt__(self, other):
        if self.date == None: return True  # Вот как решился вопрос Василия, ты мне кстати это в курсовой подсказывал
        if other.date == None: return False  # ПРИГОДИЛОСЬ )))
        return self.date < other.date

    def __gt__(self, other):
        return self.date > other.date


def set_operations(data):
    """ Функция преобразует json в экземпляры класса"""
    with open(f'{data}', 'r') as f:
        file = json.load(f)
        for item in file:
            Operation.all_operations.append(Operation(item))


def secret_card(card):
    """Функция красиво отображает номер карты """
    if card == None:
        return None
    else:
        result = card.split()

    return f'{result[-1][:4]} {result[-1][4: 6]}** **** {result[-1][13:]}'


set_operations(' operations.json')  # преобразовываем все в список с экземплярами
sorted_data = sorted(Operation.all_operations, reverse=True)  # сортируем по дате ( реализованы lt, gt)
for i in sorted_data[:5]:
    my_number = secret_card(i.from_operation)  # красиво преобразовываем номер
    print(f'{i.date[:10]} {i.description}\n {my_number} -> Счет **{i.to[-4:-1]}\n {i.operationAmount} {i.nominal}')
    print()

# 2019-12-07 Перевод организации
# 2842 87** **** 012 -> Счет **365
# 48150.39 USD
