import textwrap
from functions import *

def display_main():
    return print(textwrap.dedent(
    f"""
    [-------------------------------------------]
    [ Документ создан   ] [ 06.08.2025 13:59:22 ]
    [ Документ завершен ] [ 00.00.0000 00:00:00 ]
    [ Документ открыт   ] [ {simple_time()} ]
    [-------------------------------------------]
    [ 1 ][ Арифметические операции              ]
    [ 2 ][ Квадратное уравнение                 ]
    [ 3 ][ Факториал                            ]
    [ 4 ][ Массивы                              ]
    [ 5 ][ Матрицы                              ]
    [ 6 ][ Сумма матриц                         ]
    [ 7 ][ Шифр Цезаря (ASCII)                  ]
    [ 8 ][ Шифр Цезаря (Словарь)                ]
    [-------------------------------------------]
    [ x ][ Настройки логирования                ]
    [ y ][ ANSI Escape коды                     ]
    [ z ][ Настройки ошибок                     ]
    [-------------------------------------------]
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


def display_arithmetic_action():
    return print(textwrap.dedent(
    """
    [ 1 ] [ Сложение               ]
    [ 2 ] [ Вычитание              ]
    [ 3 ] [ Умножение              ]
    [ 4 ] [ Деление                ]
    [ 5 ] [ Целочисленное деление  ]
    [ 6 ] [ Остаток                ]
    """
    ).strip())


def display_arithmetic_input():
    try:
        a = float(input("[   Введите значение a   ] = "))
        b = float(input("[   Введите значение b   ] = "))
    except ValueError:
        print("[ Ошибка: введено недопустимое значение ]")
        a = "-"
        b = "-"
    return a, b

    
def display_arithmetic_plus(a, b):
    op, er_message, result = plus(a, b)
    print(textwrap.dedent(
    f"""
    [ Сложение ] [ {a} + {b} ] [ {result} ] [ {er_message} ]
    """
    ).strip())
    return op, er_message, result


def display_arithmetic_minus(a, b):
    op, er_message, result = minus(a, b)
    print(textwrap.dedent(
    f"""
    [ Сложение ] [ {a} + {b} ] [ {result} ] [ {er_message} ]
    """
    ).strip())
    return op, er_message, result


def display_arithmetic_multiply(a, b):
    op, er_message, result = multiply(a, b)
    print(textwrap.dedent(
    f"""
    [ Сложение ] [ {a} + {b} ] [ {result} ] [ {er_message} ]
    """
    ).strip())
    return op, er_message, result


def display_arithmetic_divide(a, b):
    op, er_message, result = divide(a, b)
    print(textwrap.dedent(
    f"""
    [ Сложение ] [ {a} + {b} ] [ {result} ] [ {er_message} ]
    """
    ).strip())
    return op, er_message, result


def display_arithmetic_full_divide(a, b):
    op, er_message, result = full_divide(a, b)
    print(textwrap.dedent(
    f"""
    [ Сложение ] [ {a} + {b} ] [ {result} ] [ {er_message} ]
    """
    ).strip())
    return op, er_message, result


def display_arithmetic_remainder(a, b):
    op, er_message, result = remainder(a, b)
    print(textwrap.dedent(
    f"""
    [ Сложение ] [ {a} + {b} ] [ {result} ] [ {er_message} ]
    """
    ).strip())
    return op, er_message, result


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
        a = "-"
        b = "-"
        c = "-"
        
    er_message, formula = square_root_formula(a, b, c)
    er_message, D = discriminant(a, b, c)
    er_message, x1, x2 = square_root_mathing(a, b, c, D)
    return er_message, formula, D, x1, x2


def display_square_root_math(formula, D, x1, x2, er_message):
    return print(textwrap.dedent(
    f"""
    [ Состояние:     ] [ {er_message} ]
    [ Формула:       ] [ {formula} ]
    [ Дискриминант:  ] [ {D} ]
    [ Первый корень: ] [ {x1} ]
    [ Второй корень: ] [ {x2} ]
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
        print("[ Ошибка: введено недопустимое значение ]")
        num = "-"
        
    er_message, factorial = fact(num)
    return num, er_message, factorial


def display_factorial_math(num, er_message, factorial):
    return print(textwrap.dedent(
    f"""
    [ Введено значение ] [ {num} ]
    [ Состояние        ] [ {er_message} ]
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
        print("[ Ошибка: введено недопустимое значение ]")
        width = "-"
    er_message, Array = array_create(width)
    return er_message, Array, width


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
        print("[ Ошибка: Введено недопустимое значение ]")
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
        print("[ Ошибка: Введено недопустимое значение ]")
        write_log("Массивы: Изменение элементов: ValueError", "Ошибка: Введено недопустимое значение")
        return Array, width
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
        print("[ Ошибка: введено недопустимое значение ]")
        a = "-"
        b = "-"
    er_message, Matrix = matrix_create(a, b)
    return er_message, Matrix


def display_matrix_math(er_message, Matrix):
    return print(textwrap.dedent(
    f"""
    [ Матрица ] [ {er_message} ] {Matrix}
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
        a1 = int(input("[ 1 ] [ Введите количество столбцов в матрице ] = "))
        b1 = int(input("[ 1 ] [ Введите количество строк в матрице ] = "))
        a2 = int(input("[ 2 ] [ Введите количество столбцов во 2 матрице ] = "))
        b2 = int(input("[ 2 ] [ Введите количество строк во 2 матрице ] = "))
    except ValueError:
        print("[ Ошибка: введено недопустимое значение ]")
        a1 = "-"
        b1 = "-"
        a2 = "-"
        b2 = "-"
    er_message, Matrix = matrix_create(a1, b1)
    er_message, Matrix2 = matrix_create(a2, b2)
    er_message, summed_matrix = matrix_sum(Matrix, Matrix2)
    return er_message, Matrix, Matrix2, summed_matrix


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
        print("[ Ошибка: введено недопустимое значение ]")
        bias = "-"
    er_message, result = caesar_ascii(start_string, bias)
    
    return start_string, bias, er_message, result


def display_caesar_ascii_math(start_string, bias, er_message, result):
    return print(textwrap.dedent(
    f"""
    [ Введенная строка     ] [ {start_string} ]
    [ Состояние            ] [ {er_message} ]
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
        print("[ Ошибка: Введено недопустимое значение ]")
        shift = "-"
    er_message, result = caesar_dictionary(text, shift)
    return text, shift, er_message, result


def display_caesar_dictionary_math(text, shift, er_message, result):
    return print(textwrap.dedent(
    f"""
    [ Введенная строка    ] [ {text} ]
    [ Состояние           ] [ {er_message} ]
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


def display_error_log_settings():
    return print(textwrap.dedent(
    """
    [------------------------------------------------------]
    [               ВЫБРАНО: Настройки ошибок              ]
    [    Файл Действия с проектом сохраняет данные ниже    ]
    [    Откройте ..saves/error_types.txt для изменения    ]
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
