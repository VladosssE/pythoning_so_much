import textwrap
from functions import *

def display_main():
    return print(textwrap.dedent(
    f"""
    [---------------------------------------------------------]
    [ Документ создан   ] [ 06.08.2025 13:59:22               ]
    [ Документ завершен ] [ 00.00.0000 00:00:00               ]
    [ Документ открыт   ] [ {simple_time()}               ]
    [---------------------------------------------------------]
    [ 1 ] [ Арифметические операции [ a ] [ Протестировать ][+]
    [ 2 ] [ Квадратное уравнение    [ b ] [ Протестировать ][+]
    [ 3 ] [ Факториал               [ c ] [ Протестировать ][+]
    [ 4 ] [ Массивы                 [ d ] [ Протестировать ][-]
    [ 5 ] [ Матрицы                 [ e ] [ Протестировать ][-]
    [ 6 ] [ Сумма матриц            [ f ] [ Протестировать ][-]
    [ 7 ] [ Шифр Цезаря (ASCII)     [ g ] [ Протестировать ][+]
    [ 8 ] [ Шифр Цезаря (Словарь)   [ h ] [ Протестировать ][+]
    [---------------------------------------------------------]
    [ x ] [ Настройки логирования                             ]
    [ z ] [ ANSI Escape коды                                  ]
    [---------------------------------------------------------]
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
        a = "ОШИБКА"
        b = "ОШИБКА"
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
        print("\033[31m[ Ошибка: введено не числовое значение ]\033[0m")
        write_log("Матрицы: ValueError", "Ошибка: Введено не числовое значение")
        a = 0
        b = 0
    Matrix = matrix_create(a, b)
    return Matrix


def display_matrix_math(Matrix):
    return print(textwrap.dedent(
    f"""
    [ Матрица ] {Matrix}
    """
    ).strip())


def display_sum_matrix():
    return print(textwrap.dedent(
    """
    [------------------------------------------------------]
    [                ВЫБРАНО: Сумма матриц                 ]
    [           Суммирует две созданные матрицы            ]
    [------------------------------------------------------]
    """
    ).strip())


def display_sum_matrix_input():
    try:
        a1 = int(input("[ Введите количество столбцов в матрице ] = "))
        b1 = int(input("[ Введите количество строк в матрице ] = "))
        a2 = int(input("[ Введите количество столбцов во 2 матрице ] = "))
        b2 = int(input("[ Введите количество строк во 2 матрице ] = "))
    except ValueError:
        print("\033[31m[ Ошибка: введено не числовое значение ]\033[0m")
        write_log("Сумма матриц: ValueError", "Ошибка: Введено не числовое значение")
        a1 = 1
        b1 = 1
        a2 = 1
        b2 = 1
    Matrix = matrix_create(a1, b1)
    Matrix2 = matrix_create(a2, b2)
    summed_matrix = matrix_sum(Matrix, Matrix2)
    return Matrix, Matrix2, summed_matrix


def display_sum_matrix_math(Matrix, Matrix2, summed_matrix):
    return print(textwrap.dedent(
    f"""
    [ Первая матрица ] {Matrix}
    [ Вторая матрица ] {Matrix2}
    [ Сумма 2 матриц ] {summed_matrix}
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


def display_testing_arithmetic():
    return print(textwrap.dedent(
    """
    [------------------------------------------------------]
    [             ВЫБРАНО: Тестирование функций            ]
    [     Тестирует все функции, вводя различные данные    ]
    [      ВЫБРАННАЯ ФУНКЦИЯ: Арифметические операции      ]
    [------------------------------------------------------]
    """
    ).strip())


def display_testing_arithmetic_math():
    print("[ Сложение ][ a = 1, b = 1 ] =",plus(1, 1))
    print("[ Сложение ][ a = 1, b = 0 ] =",plus(1, 0))
    print("[ Сложение ][ a = 1, b = t ] =",plus(1, "t"))
    print("[ Сложение ][ a = 0, b = t ] =",plus(0, "t"))
    print()
    print("[ Вычитание ][ a = 1, b = 1 ] =",minus(1, 1))
    print("[ Вычитание ][ a = 1, b = 0 ] =",minus(1, 0))
    print("[ Вычитание ][ a = 1, b = t ] =",minus(1, "t"))
    print("[ Вычитание ][ a = 0, b = t ] =",minus(0, "t"))
    print()
    print("[ Деление ][ a = 1, b = 1 ] =",divide(1, 1))
    print("[ Деление ][ a = 1, b = 0 ] =",divide(1, 0))
    print("[ Деление ][ a = 1, b = t ] =",divide(1, "t"))
    print("[ Деление ][ a = 0, b = t ] =",divide(0, "t"))
    print()
    print("[ Целочисленное деление ][ a = 1, b = 1 ] =",full_divide(1, 1))
    print("[ Целочисленное деление ][ a = 1, b = 0 ] =",full_divide(1, 0))
    print("[ Целочисленное деление ][ a = 1, b = t ] =",full_divide(1, "t"))
    print("[ Целочисленное деление ][ a = 0, b = t ] =",full_divide(0, "t"))
    print()
    print("[ Умножение ][ a = 1, b = 1 ] =",multiply(1, 1))
    print("[ Умножение ][ a = 1, b = 0 ] =",multiply(1, 0))
    print("[ Умножение ][ a = 1, b = t ] =",multiply(1, "t"))
    print("[ Умножение ][ a = 0, b = t ] =",multiply(0, "t"))
    print()
    print("[ Нахождение остатка ][ a = 1, b = 1 ] =",remainder(1, 1))
    print("[ Нахождение остатка ][ a = 1, b = 0 ] =",remainder(1, 0))
    print("[ Нахождение остатка ][ a = 1, b = t ] =",remainder(1, "t"))
    print("[ Нахождение остатка ][ a = 0, b = t ] =",remainder(0, "t"))
    return 0


def display_testing_square_root():
    return print(textwrap.dedent(
    """
    [------------------------------------------------------]
    [             ВЫБРАНО: Тестирование функций            ]
    [     Тестирует все функции, вводя различные данные    ]
    [       ВЫБРАННАЯ ФУНКЦИЯ: Квадратное уравнение        ]
    [------------------------------------------------------]
    """
    ).strip())


def display_testing_square_root_math():
    print("[ Формула ][ a = 1, b = 1, c = 1 ] =",square_root_formula(1, 1, 1))
    print("[ Формула ][ a = 0, b = 0, c = 0 ] =",square_root_formula(0, 0, 0))
    print("[ Формула ][ a = t, b = 1, c = 0 ] =",square_root_formula("t", 1, 0))
    print()
    print("[ Дискриминант ][ a = 1, b = 1, c = 1 ] =",discriminant(1, 1, 1))
    print("[ Дискриминант ][ a = 0, b = 0, c = 0 ] =",discriminant(0, 0, 0))
    print("[ Дискриминант ][ a = t, b = 1, c = 0 ] =",discriminant("t", 1, 0))
    print()
    print("[ Решение ][ a = 1, b = 1, c = 1, D = 1 ] =",square_root_mathing(1, 1, 1, 1))
    print("[ Решение ][ a = 1, b = 1, c = 1, D = 0 ] =",square_root_mathing(1, 1, 1, 0))
    print("[ Решение ][ a = 1, b = 1, c = 1, D = -1 ] =",square_root_mathing(1, 1, 1, -1))
    print("[ Решение ][ a = 0, b = 0, c = 0, D = 0 ] =",square_root_mathing(0, 0, 0, 0))
    print("[ Решение ][ a = t, b = 1, c = 0, D = t ] =",square_root_mathing("t", 1, 0, "t"))
    return 0


def display_testing_factorial():
    return print(textwrap.dedent(
    """
    [------------------------------------------------------]
    [             ВЫБРАНО: Тестирование функций            ]
    [     Тестирует все функции, вводя различные данные    ]
    [             ВЫБРАННАЯ ФУНКЦИЯ: Факториал             ]
    [------------------------------------------------------]
    """
    ).strip())


def display_testing_factorial_math():
    print("[ a = 5  ] =",fact(5))
    print("[ a = 0  ] =",fact(0))
    print("[ a = -5 ] =",fact(-5))
    print("[ a = t  ] =",fact("t"))
    return 0


def display_testing_array():
    return print(textwrap.dedent(
    """
    [------------------------------------------------------]
    [             ВЫБРАНО: Тестирование функций            ]
    [     Тестирует все функции, вводя различные данные    ]
    [              ВЫБРАННАЯ ФУНКЦИЯ: Массивы              ]
    [------------------------------------------------------]
    """
    ).strip())


def display_testing_array_math():
    return print("\u001b[36m[ Тестирование данной функции пока что не написано ]\u001b[0m")


def display_testing_matrix():
    return print(textwrap.dedent(
    """
    [------------------------------------------------------]
    [             ВЫБРАНО: Тестирование функций            ]
    [     Тестирует все функции, вводя различные данные    ]
    [              ВЫБРАННАЯ ФУНКЦИЯ: Матрицы              ]
    [------------------------------------------------------]
    """
    ).strip())


def display_testing_matrix_math():
    return print("\u001b[36m[ Тестирование данной функции пока что не написано ]\u001b[0m")


def display_testing_sum_matrix():
    return print(textwrap.dedent(
    """
    [------------------------------------------------------]
    [             ВЫБРАНО: Тестирование функций            ]
    [     Тестирует все функции, вводя различные данные    ]
    [            ВЫБРАННАЯ ФУНКЦИЯ: Сумма матриц           ]
    [------------------------------------------------------]
    """
    ).strip())


def display_testing_sum_matrix_math():
    return print("\u001b[36m[ Тестирование данной функции пока что не написано ]\u001b[0m")


def display_testing_caesar_ascii():
    return print(textwrap.dedent(
    """
    [------------------------------------------------------]
    [             ВЫБРАНО: Тестирование функций            ]
    [     Тестирует все функции, вводя различные данные    ]
    [        ВЫБРАННАЯ ФУНКЦИЯ: Шифр Цезаря (ASCII)        ]
    [------------------------------------------------------]
    """
    ).strip())


def display_testing_caesar_ascii_math():
    print("[ Строка = 'apple', Смещение = '3'  ] =",caesar_ascii("apple", 3))
    print("[ Строка = 'apple', Смещение = '0'  ] =",caesar_ascii("apple", 0))
    print("[ Строка = 'apple', Смещение = '-3' ] =",caesar_ascii("apple", -3))
    print("[ Строка = 'apple', Смещение = '-70' ] =",caesar_ascii("apple", -70))
    print("[ Строка = 'apple', Смещение = '122' ] =",caesar_ascii("apple", 122))
    print("[ Строка = 'apple', Смещение = 't' ] =",caesar_ascii("apple", "t"))
    return 0


def display_testing_caesar_dictionary():
    return print(textwrap.dedent(
    """
    [------------------------------------------------------]
    [             ВЫБРАНО: Тестирование функций            ]
    [     Тестирует все функции, вводя различные данные    ]
    [       ВЫБРАННАЯ ФУНКЦИЯ: Шифр Цезаря (Словарь)       ]
    [------------------------------------------------------]
    """
    ).strip())


def display_testing_caesar_dictionary_math():
    print("[ Строка = 'apple', Смещение = '3'  ] =",caesar_dictionary("apple", 3))
    print("[ Строка = 'apple', Смещение = '0'  ] =",caesar_dictionary("apple", 0))
    print("[ Строка = 'apple', Смещение = '-3' ] =",caesar_dictionary("apple", -3))
    print("[ Строка = 'apple', Смещение = '-70' ] =",caesar_dictionary("apple", -70))
    print("[ Строка = 'apple', Смещение = '122' ] =",caesar_dictionary("apple", 122))
    print("[ Строка = 'apple', Смещение = 't' ] =",caesar_dictionary("apple", "t"))
    return 0
