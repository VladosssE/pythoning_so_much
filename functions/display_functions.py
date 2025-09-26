import textwrap
from time import localtime, strftime
from .arithmetic_operations import *

def simple_time():
    current_time = strftime("%d.%m.%Y %H:%M:%S", localtime())
    return current_time


def display_main():
    return print(textwrap.dedent(
    f"""
    [----------------------------------------------------]
    [ Документ создан   ] [ 06 Август 2025 13:59:22      ]
    [ Документ завершен ] [ 00.00.0000 00:00:00          ]
    [ Документ открыт   ] [ {simple_time()}          ]
    [----------------------------------------------------]
    [ Выберите раздел, который вы хотите прочитать:      ]
    [ 1 ] [ Арифметические операции                      ]
    [ 2 ] [ Квадратное уравнение                         ]
    [ 3 ] [ Факториал                                    ]
    [ 4 ] [ Массивы                                      ]
    [ 0 ] [ Настройки логирования                        ]
    """
    ).strip())


def display_arithmetic():
    return print(textwrap.dedent(
    """
    [ ВЫБРАНО: Арифметические операции ]
    [ Выводит результаты базовых арифметических операций ]
    """
    ).strip())


def display_arithmetic_math(a, b):
    return print(textwrap.dedent(
    f"""
    Сложение:              {a} + {b}  = {plus(a, b)}
    Вычитание:             {a} - {b}  = {minus(a, b)}
    Умножение:             {a} * {b}  = {multiply(a, b)}
    Деление:               {a} / {b}  = {divide(a, b)}
    Целочисленное деление: {a} // {b} = {full_divide(a, b)}
    Нахождение остатка:    {a} % {b}  = {remainder(a, b)}
    """
    ).strip())


def display_square_root():
    return print(textwrap.dedent(
    """
    [ ВЫБРАНО: Квадратное уравнение ]
    [ Решает полное квадратное уравнение ]
    """
    ).strip())


def display_square_root_math(formula, D, result):
    return print(textwrap.dedent(
    f"""
    Формула: {formula}
    Дискриминант: {D}
    Ответ: {result}
    """
    ).strip())


def display_factorial():
    return print(textwrap.dedent(
    """
    [ ВЫБРАНО: Факториал ]
    [ Выводит факториал числа ]
    """
    ).strip())


def display_factorial_math(num, factorial):
    return print(textwrap.dedent(
    f"""
    Введено значение = {num}
    Факториал равен = {factorial}
    """
    ).strip())


def display_array():
    return print(textwrap.dedent(
    """
    [ ВЫБРАНО: Массивы ] 
    [ Выводит простой массив из введенных значений ]
    [ Пример: ['0', '1', '2'] ]
    """
    ).strip())


def display_array_math(Array):
    return print(textwrap.dedent(
    f"""
    Массив = {Array}
    """
    ).strip())
