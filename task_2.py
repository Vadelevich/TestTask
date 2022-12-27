def func(list):
    """ Функция  принимает массив и перемещает нули в конец, сохраняя порядок остальных элементов"""
    count = 0
    for i in list:
        if i == 0:
            count += 1
    new_list = list[count:] + list[:count]
    return new_list


def row_sum(n: int):
    """ Функция считает сумму н-го ряда пирамиды нечетных чисел (начало с 1)"""
    prev_row: list[int] = []  # Список чисел до требуемого ряда
    n_row: list[int] = []  # Список чисел который будем суммировать (н-ый ряд)

    if n > 1:  # Если нет, сразу вернем 1
        for i in range(1, n * (n - 1),
                       2):  # step = 2, так как используется нечетная последовательность чисел, n*(n-1) выход из цикла не доходя последнего ряда
            prev_row.append(i)

        for i in range(prev_row[-1] + 2, prev_row[-1] + (n * 2) + 2,
                       2):  # prev_row - узнаем последнее число на котором остановились (первый член n-го ряда)
            n_row.append(i)  #
    else:  #
        n_row.append(n)  #

    return sum(n_row)  # в n_row хранятся члены исключительно n-го ряда,посчитаем сумму


list = [0, 0, 0, 1, 2, 6, 4, 3, 6]

print(func(list))
print(row_sum(4))
