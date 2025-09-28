import textwrap
from functions import *


def display_main():
    return print(textwrap.dedent(
    f"""
    [------------------------------------------------------]
    [ Документ создан   ] [ 06.08.2025 13:59:22            ]
    [ Документ завершен ] [ 00.00.0000 00:00:00            ]
    [ Документ открыт   ] [ {simple_time()}            ]
    [------------------------------------------------------]
    [ 1 ] [ Арифметические операции                        ]
    [ 2 ] [ Квадратное уравнение                           ]
    [ 3 ] [ Факториал                                      ]
    [ 4 ] [ Массивы                                        ]
    [ 5 ] [ Матрицы                                        ]
    [ 6 ] [ Шифр Цезаря (ASCII)                            ]
    [ 7 ] [ Шифр Цезаря (Словарь)                          ]
    [ a ] [ Настройки логирования                          ]
    [ b ] [ ANSI Escape коды                               ]
    [------------------------------------------------------]
    """
    ).strip())


def display_arithmetic():
    return print(textwrap.dedent(
    """
    [------------------------------------------------------]
    [           ВЫБРАНО: Арифметические операции           ]
    [  Выводит результаты базовых арифметических операций  ]
    [------------------------------------------------------]
    """
    ).strip())


def display_arithmetic_input():
    try:
        a = float(input("[   Введите значение a   ] = "))
        b = float(input("[   Введите значение b   ] = "))
    except ValueError:
        print("\u001b[31m[ Ошибка: Введено не числовое значение ]\u001b[0m")
        write_log("Арифметические операции: ValueError", "Ошибка: Введено не числовое значение")
        a = 0
        b = 0
        return a, b
    return a, b

    
def display_arithmetic_math(a, b):
    return print(textwrap.dedent(
    f"""
    [ Сложение:              ] [ {a} + {b}  ] [ {plus(a, b)} ]
    [ Вычитание:             ] [ {a} - {b}  ] [ {minus(a, b)} ]
    [ Умножение:             ] [ {a} * {b}  ] [ {multiply(a, b)} ]
    [ Деление:               ] [ {a} / {b}  ] [ {divide(a, b)} ]
    [ Целочисленное деление: ] [ {a} // {b} ] [ {full_divide(a, b)} ]
    [ Нахождение остатка:    ] [ {a} % {b}  ] [ {remainder(a, b)} ]
    """
    ).strip())


def display_square_root():
    return print(textwrap.dedent(
    """
    [------------------------------------------------------]
    [            ВЫБРАНО: Квадратное уравнение             ]
    [          Решает полное квадратное уравнение          ]
    [------------------------------------------------------]
    """
    ).strip())


def display_square_root_input():
    try:
        a = int(input("[ Введите значение a ] = "))
        b = int(input("[ Введите значение b ] = "))
        c = int(input("[ Введите значение c ] = "))
    except ValueError:
        print("\033[31m[ Ошибка: Введено не числовое значение ]\033[0m")
        write_log("Квадратное уравнение: ValueError", "Ошибка: Введено не числовое значение")
        a = 1
        b = 1
        c = 1
        
    formula = square_root_formula(a, b, c)
    D = discriminant(a, b, c)
    result = square_root_mathing(a, b, c, D)
    return formula, D, result


def display_square_root_math(formula, D, result):
    return print(textwrap.dedent(
    f"""
    [ Формула:      ] [ {formula} ]
    [ Дискриминант: ] [ {D} ]
    [ Ответ:        ] [ {result} ]
    """
    ).strip())


def display_factorial():
    return print(textwrap.dedent(
    """
    [------------------------------------------------------]
    [                  ВЫБРАНО: Факториал                  ]
    [                Выводит факториал числа               ]
    [------------------------------------------------------]
    """
    ).strip())


def display_factorial_input():
    try:
        num = int(input("[ Введите число ] = "))
    except ValueError:
        print("\033[31m[ Ошибка: Введено не числовое значение ]\033[0m")
        write_log("Факториал: ValueError", "Ошибка: Введено не числовое значение")
        num = 1
        
    factorial = fact(num)
    return num, factorial


def display_factorial_math(num, factorial):
    return print(textwrap.dedent(
    f"""
    [ Введено значение ] [ {num} ]
    [ Факториал равен  ] [ {factorial} ]
    """
    ).strip())


def display_array():
    return print(textwrap.dedent(
    """
    [------------------------------------------------------]
    [                   ВЫБРАНО: Массивы                   ] 
    [     Выводит простой массив из введенных значений     ]
    [------------------------------------------------------]
    """
    ).strip())


def display_array_input():
    try:
        width = int(input("[ Введите количество элементов в массиве ] = "))
    except ValueError:
        print("\033[31m[ Ошибка: Введено не числовое значение ]\033[0m")
        write_log("Массив: ValueError", "Ошибка: Введено не числовое значение")
        width = 0
    Array = array_create(width)
    return Array, width


def display_array_math(Array):
    return print(textwrap.dedent(
    f"""
    [ Массив ] {Array}
    """
    ).strip())


def display_array_actions():
    return print(textwrap.dedent(
    """
    [ 1 ] [ Поиск по массиву                               ]
    [ 2 ] [ Добавление элементов                           ]
    [ 3 ] [ Изменение элементов                            ]
    [ 4 ] [ Удаление элементов                             ]
    [ 5 ] [ Выход                                          ]
    """
    ).strip())


def display_array_item_find(Array, width):
    print(f"Текущий массив: {Array}")
    target = input("Что вы хотите найти? > ")
    print(array_find(Array, target))
    return Array, width


def display_array_item_add(Array, width):
    print(f"Текущий массив: {Array}")
    try:
        add = input("Какой элемент хотите добавить? > ")
        pos = int(input("В какую позицию хотите добавить? > "))
    except ValueError:
        print("\033[31m[ Ошибка: Введено недопустимое значение ]\033[0m")
        write_log("Массивы: Добавление элементов: ValueError", "Ошибка: Введено недопустимое значение")
        return Array, width
    print(array_add(Array, add, pos))
    return Array, width


def display_array_item_change(Array, width):
    print(f"Текущий массив: {Array}")
    try:
        pos = int(input("В какой позиции хотите изменить значение? > "))
        change = input("Новое значение > ")
    except ValueError:
        print("\033[31m\n[ Ошибка: Введено недопустимое значение ]\033[0m")
        write_log("Массивы: Изменение элементов: ValueError", "Ошибка: Введено недопустимое значение")
        return array_actions(Array, width)
    print(array_change(Array, change, pos, width))
    return Array, width


def display_array_item_delete(Array, width):
    print(f"Текущий массив: {Array}")
    delete = input("Какой элемент вы хотите удалить? > ")
    print(array_delete(Array, delete, width))
    return Array, width


def display_matrix():
    return print(textwrap.dedent(
    """
    [------------------------------------------------------]
    [                   ВЫБРАНО: Матрицы                   ]
    [     Выводит простую матрицу из введенных значений    ]
    [------------------------------------------------------]
    """
    ).strip())


def display_matrix_input():
    try:
        a = int(input("[ Введите количество столбцов в матрице ] = "))
        b = int(input("[ Введите количество строк в матрице ] = "))
    except ValueError:
        print("\033[31m\n[ Ошибка: введено не числовое значение ]\033[0m")
        write_log("Матрицы: ValueError", "Ошибка: Введено не числовое значение")
    Matrix = matrix_create(a, b)
    return Matrix


def display_matrix_math(Matrix):
    return print(textwrap.dedent(
    f"""
    [ Матрица ] {Matrix}
    """
    ).strip())


def display_caesar_ascii():
    return print(textwrap.dedent(
    f"""
    [------------------------------------------------------]
    [             ВЫБРАНО: Шифр Цезаря (ASCII)             ]
    [   Шифрует введенную строку, используя шифр Цезаря    ]
    [------------------------------------------------------]
    """
    ).strip())


def display_caesar_ascii_input():
    try:
        start_string = input("[ Введите строку ] = ")
        bias = int(input("[ Введите количество смещений ] = "))
    except ValueError:
        print("\033[31m[ Ошибка: введено недопустимое значение ]\033[0m")
        start_string = "ERROR"
        bias = 0
    result = caesar_ascii(start_string, bias)
    
    return start_string, bias, result


def display_caesar_ascii_math(start_string, bias, result):
    return print(textwrap.dedent(
    f"""
    [ Введенная строка     ] [ {start_string} ]
    [ Смещение             ] [ {bias} ]
    [ Зашифрованная строка ] [ {result} ]
    """
    ).strip())


def display_caesar_dictionary():
    return print(textwrap.dedent(
    f"""
    [------------------------------------------------------]
    [            ВЫБРАНО: Шифр Цезаря (Словарь)            ]
    [    Шифрует введенную строку, используя шифр Цезаря   ]
    [------------------------------------------------------]
    """
    ).strip())


def display_caesar_dictionary_input():
    try:
        text = input("Введите строку: ")
        shift = int(input("Введите количество смещений: "))
    except ValueError:
        print("\033[31m[ Ошибка: Введено недопустимое значение ]\033[0m")
        write_log("Шифр Цезаря (Словарь): ValueError", "Ошибка: Введено не числовое значение")
        text = "ERROR"
        shift = "0"
    result = caesar_dictionary(text, shift)
    return text, shift, result


def display_caesar_dictionary_math(text, shift, result):
    return print(textwrap.dedent(
    f"""
    [ Введенная строка    ] [ {text} ]
    [ Количество смещений ] [ {shift} ]
    [ Полученная строка   ] [ {result} ]
    """
    ).strip())


def display_log_settings():
    return print(textwrap.dedent(
    """
    [------------------------------------------------------]
    [            ВЫБРАНО: Настройки логирования            ]
    [    Файл Действия с проектом сохраняет данные ниже    ]
    [     Откройте ..saves/log_types.txt для изменения     ]
    [------------------------------------------------------]
    """
    ).strip())


def display_ansi_escape_codes():
    print("[","".center(50, "-"),"]")
    print("[","ВЫБРАНО: ANSI Escape коды".center(50),"]")
    print("[","Используются для вывода цветного текста в консоли".center(50),"]")
    print("[","".center(50, "-"),"]")
    print("[ \u001b[30mЧерный цвет текста\u001b[0m         ]",r"[ \u001b[30m    ] [ Ч ]")
    print("[ \u001b[31mКрасный цвет текста\u001b[0m        ]",r"[ \u001b[31m    ] [ К ]")
    print("[ \u001b[32mЗеленый цвет текста\u001b[0m        ]",r"[ \u001b[32m    ] [ З ]")
    print("[ \u001b[33mЖелтый цвет текста\u001b[0m         ]",r"[ \u001b[33m    ] [ Ж ]")
    print("[ \u001b[34mСиний цвет текста\u001b[0m          ]",r"[ \u001b[34m    ] [ С ]")
    print("[ \u001b[35mПурпурный цвет текста\u001b[0m      ]",r"[ \u001b[35m    ] [ П ]")
    print("[ \u001b[36mГолубой цвет текста\u001b[0m        ]",r"[ \u001b[36m    ] [ Г ]")
    print("[ \u001b[37mБелый цвет текста\u001b[0m          ]",r"[ \u001b[37m    ] [ Б ]")
    print("[","".center(50, "-"),"]")
    print("[ \u001b[30;1mЯрко черный цвет текста\u001b[0m    ]",r"[ \u001b[30;1m  ] [ Ч ]")
    print("[ \u001b[31;1mЯрко красный цвет текста\u001b[0m   ]",r"[ \u001b[31;1m  ] [ К ]")
    print("[ \u001b[32;1mЯрко зеленый цвет текста\u001b[0m   ]",r"[ \u001b[32;1m  ] [ З ]")
    print("[ \u001b[33;1mЯрко желтый цвет текста\u001b[0m    ]",r"[ \u001b[33;1m  ] [ Ж ]")
    print("[ \u001b[34;1mЯрко синий цвет текста\u001b[0m     ]",r"[ \u001b[34;1m  ] [ С ]")
    print("[ \u001b[35;1mЯрко пурпурный цвет текста\u001b[0m ]",r"[ \u001b[35;1m  ] [ П ]")
    print("[ \u001b[36;1mЯрко голубой цвет текста\u001b[0m   ]",r"[ \u001b[36;1m  ] [ Г ]")
    print("[ \u001b[37;1mЯрко белый цвет текста\u001b[0m     ]",r"[ \u001b[37;1m  ] [ Б ]")
    print("[","".center(50, "-"),"]")
    print("[ \u001b[40mЧерный цвет фона\u001b[0m           ]",r"[ \u001b[40m    ] [ Ч ]")
    print("[ \u001b[41mКрасный цвет фона\u001b[0m          ]",r"[ \u001b[41m    ] [ К ]")
    print("[ \u001b[42mЗеленый цвет фона\u001b[0m          ]",r"[ \u001b[42m    ] [ З ]")
    print("[ \u001b[43mЖелтый цвет фона\u001b[0m           ]",r"[ \u001b[43m    ] [ Ж ]")
    print("[ \u001b[44mСиний цвет фона\u001b[0m            ]",r"[ \u001b[44m    ] [ С ]")
    print("[ \u001b[45mПурпурный цвет фона\u001b[0m        ]",r"[ \u001b[45m    ] [ П ]")
    print("[ \u001b[46mГолубой цвет фона\u001b[0m          ]",r"[ \u001b[46m    ] [ Г ]")
    print("[ \u001b[47mБелый цвет фона\u001b[0m            ]",r"[ \u001b[47m    ] [ Б ]")
    print("[","".center(50, "-"),"]")
    return 0
