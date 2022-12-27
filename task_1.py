import re  # Добавлен импорт re


def to_camel_case(text):
    """ Первое задание """
    return re.split('_|-', text)[1] + ''.join(word.title() for word in re.split('_|-', "text")[1::])  # Исправлен отступ


class SingletonMeta(type):
    """ Реализация Singleton с метклассами """
    _instances = {}

    def __call__(cls, *args, **kwargs):  # специальный метод __call__ используется в метаклассе для создания Singleton.
        if cls not in cls._instances:  # Добавлено отрицание not
            instance = super().__call__(*args, **kwargs)  # исправлен магический метод __call__
            cls._instances[cls] = instance
        return cls._instances[cls]


count_bits = lambda n: bin(n).count('1')  # Добавлен аргумент у lambda функции


def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int, str(n))))  # Исправлен if , исправлена функция/метод? sum


even_or_odd = lambda number: "Even" if number % 2 == 0 else "Odd"  # Исправлен if
