from time import localtime, strftime
from math import sqrt
import os

#Функция "Арифметические операции"
def arithmetic_operations():
    current_time = strftime("%d.%m.%Y в %H:%M:%S", localtime())
    print("[","ВЫБРАНО: Арифметические операции".center(50),"]")
    print("[ Выводит результаты базовых арифметических операций ]\n")
    
    try:
        a = int(input("Введите значение a: "))  
        b = int(input("Введите значение b: "))
    except ValueError:
        print("\033[31m\n[ Ошибка: Введено не числовое значение ]\033[0m") # \033[31m - ANSI Escape код для вывода красного цвета текста
        return arithmetic_operations()
    
    c1 =(
        f"\nСложение = {a} + {b} = {a + b}\n"
        +f"Вычитание = {a} - {b} = {a - b}\n"
        +f"Умножение = {a} * {b} = {a * b}\n"
        )

    try:
        c2_ab = a/b
        c2_ba = b/a
    except ZeroDivisionError:
        print("\u001b[33m\n[ Внимание: Деление на ноль невозможно ]\u001b[0m")
        c2_ab = c2_ba = None

    if c2_ab is not None and c2_ba is not None:
        c2 = (
             f"Деление {a} / {b} = {a/b:.2f}\n"
             +f"Целочисленное деление {a} // {b} = {a//b}\n"
             +f"Нахождение остатка {a} % {b} = {a%b}"
             )
    else:
        c2 = (
            f"Деление {a} / {b} невозможно\n"
            + f"Целочисленное деление {a} // {b} невозможно\n"
            + f"Нахождение остатка {a} % {b} невозможно\n"
        )
    #Выводится только 2 знака после запятой в результате деления.
    #Для изменения количества меняйте число перед знаком f (b:.2f)
    print(c1 + c2)
    
    with open("Использование функции Арифметические операции.txt","a") as ao_file:
        ao_file.write(f"Данные получены: {current_time}{c1}{c2}\n\n")
    
    try:
        d = int(input("\n[ 1 ] Повторить\n[ 2 ] Вернуться\n> "))
    except ValueError:
        print("\033[31m[ Ошибка: Введено не числовое значение ]\033[0m")
        return arithmetic_operations()
    if d == 1:
        clear_console()
        arithmetic_operations()
    elif d == 2:
        clear_console()
        starting_point()

    return "Выход из функции"


#Функция "Условные операторы"
def if_elses():
    current_time = strftime("%d.%m.%Y в %H:%M:%S", localtime())
    print("[","ВЫБРАНО: Условные операторы".center(50),"]")
    print("[","Решает полное квадратное уравнение".center(50),"]")
    print(
        "Уравнение имеет вид ax^2 + bx + c = 0\n"
        +"D = b^2 - 4ac\n"
        +"D > 0: Два различных корня\n"
        +"D = 0: Один корень\n"
        +"D < 0: Корней нет\n"
        +"x1 = (-b + Корень из D) / 2a\n"
        +"x2 = (-b - Корень из D) / 2a\n"
        )
    
    try:
        a = int(input("Введите значение a: "))
        b = int(input("Введите значение b: "))
        c = int(input("Введите значение c: "))
    except ValueError:
        print("\033[31m\n[ Ошибка: Введено не числовое значение ]\033[0m")
        return if_elses()

    if a == 0 or b == 0 or c == 0:
        print("\u001b[33m\n[ Программа не может решать неполные квадратные уравнения ]\u001b[0m")
        return if_elses()
    
    num = f"{a}x^2 + {b}x + {c} = 0"
    D = b**2 - 4*a*c
    print(num)
    print(f"D = {D}")

    if D > 0:
        x1 = (-b + sqrt(D)) / (2*a)
        x2 = (-b - sqrt(D)) / (2*a)
        print(f"Первый корень = {x1:.2f}\nВторой корень = {x2:.2f}")
    elif D == 0:
        x1 = (-b + sqrt(D)) / (2*a)
        x2 = 0
        print(f"Корень = {x1:.2f}")
    elif D < 0:
        print("Корней нет")
        x1 = 0
        x2 = 0

    with open("Использование функции Условные операторы.txt","a") as ie_file:
        ie_file.write(
                     f"Данные получены: {current_time}\n"
                     +f"{num}\nДискриминант = {D}\n"
                     +f"Первый корень = {x1}\n"
                     +f"Второй корень = {x2}\n\n"
                     )

    try:
        d = int(input("\n[ 1 ] Повторить\n[ 2 ] Вернуться\n> "))
    except ValueError:
        print("\033[31m[ Ошибка: Введено не числовое значение ]\033[0m")
        return if_elses()
    
    if d == 1:
        clear_console()
        if_elses()
    elif d == 2:
        clear_console()
        starting_point()
    return "Выход из функции"


#функция "Циклы"
def loops():
    current_time = strftime("%d.%m.%Y в %H:%M:%S", localtime())
    fact = 1
    print("[","ВЫБРАНО: Циклы".center(50),"]")
    print("[","Выводит факториал числа".center(50),"]")
    
    try:
        a = int(input("Введите число: "))
    except ValueError:
        print("\033[31m\n[ Ошибка: Введено не числовое значение ]\033[0m")
        return loops()
    
    if a < 0:
        print("\u001b[33m\n[ Для отрицательных чисел нет факториала ]\u001b[0m")
        fact = "Не определен"
    elif a == 0:
        print("\u001b[33m\n[ Факториал 0 равен 1 ]\u001b[0m")
        fact = 1
    else:
        for i in range(1, a+1):
            fact = fact * i
        print(f"Факториал {a} равен {fact}")
    
    with open("Использование функции Циклы.txt","a") as c_file:
        c_file.write(
                    f"Данные получены: {current_time}\n"
                    +f"Введено число: {a}\n"
                    +f"Факториал равен: {fact}\n\n"
                    )

    try:
        d = int(input("\n[ 1 ] Повторить\n[ 2 ] Вернуться\n> "))
    except ValueError:
        print("\033[31m[ Ошибка: Введено не числовое значение ]\033[0m")
        return loops()
    if d == 1:
        clear_console()
        loops()
    elif d == 2:
        clear_console()
        starting_point()
    return "Выход из функции"


#Функция "Массивы"
def arrays():
    current_time = strftime("%d.%m.%Y в %H:%M:%S", localtime())
    print("[","ВЫБРАНО: Массивы".center(50),"]")
    print("[","Выводит простой массив из введенных значений".center(50),"]")
    print("[","Пример: ['0', '1', '2']".center(50),"]")
    Array = []
    
    try:
        a = int(input("Введите количество элементов в массиве: "))
    except ValueError:
        print("\033[31m\n[ Ошибка: Введено не числовое значение ]\033[0m")
        return arrays()
    
    if a == 0:
        print("\u001b[33m\n[ Количество элементов массива: 0 ]\u001b[0m")
        Array = "[Создание массива провалилось]"
    elif a < 0:
        print("\033[31m\n[ Ошибка: отрицательное количество элементов массива ]\033[0m")
        Array = "[Создание массива провалилось]"
    else:
        for i in range(a):
            try:
                b = input("Введите элементы массива: ")
            except ValueError:
                print("\033[31m\n[ Ошибка: введено недопустимое значение (???) ]\033[0m")
                return arrays()
            Array.append(b)
        print(f"Массив: {Array}")
        
    with open("Использование функции Массивы.txt","a") as ar_file:
        ar_file.write(
                      f"Данные получены: {current_time}\n"
                      +f"Количество элементов массива: {a}\n"
                      +f"Элементы: {Array}\n\n"
                      )
    
    try:
        d = int(input("\n[ 1 ] Повторить\n[ 2 ] Вернуться\n> "))
    except ValueError:
        print("\033[31m[ Ошибка: Введено не числовое значение ]\033[0m")
        return arrays()
    if d == 1:
        clear_console()
        arrays()
    elif d == 2:
        clear_console()
        starting_point()
    return "Выход из функции"


#Функция "Матрицы"
def matrix():
    current_time = strftime("%d.%m.%Y в %H:%M:%S", localtime())
    print("[","ВЫБРАНО: Матрицы".center(50),"]")
    print("[","Выводит простую матрицу из введенных значений".center(50),"]")
    print("[","Пример: [['0', '1', '2']['3', '4', '5']['6', '7', '8']]".center(50),"]")
    Matrix = []
    
    try:
        a = int(input("Введите количество столбцов в матрице: "))
        b = int(input("Введите количество строк в матрице: "))
    except ValueError:
        print("\033[31m\n[ Ошибка: введено недопустимое значение ]\033[0m")
        matrix()
    
    if a == 0 or b == 0:
        print("\u001b[33m\n[ Значения длины либо ширины матрицы равны нулю ]\u001b[0m")
    elif a < 0 or b < 0:
        print("\033[31m\n[ Ошибка: отрицательная ширина либо длина матрицы ]\033[0m")
    else:
        for i in range(a):
            n = []
            for j in range(b):
                try:
                    m = input("Введите элементы матрицы: ")
                except ValueError:
                    print("\033[31m\n[ Введено недопустимое значение (???) ]\033[0m")
                    matrix()
                n.append(m)
            Matrix.append(n)
    print(Matrix)

    with open("Использование функции Матрицы.txt","a") as mat_file:
        mat_file.write(
            f"Данные получены: {current_time}\n"
            +f"Количество столбцов в матрице: {a}\n"
            +f"Количество строк в матрице: {b}\n"
            +f"Матрица: {Matrix}\n\n"
            )
    
    try:
        d = int(input("\n[ 1 ] Повторить\n[ 2 ] Вернуться\n> "))
    except ValueError:
        print("\033[31m[ Ошибка: Введено не числовое значение ]\033[0m")
        return matrix()
    if d == 1:
        clear_console()
        matrix()
    elif d == 2:
        clear_console()
        starting_point()
    return "Выход из функции"


#Функция "ANSI Escape коды"
def ansies():
    clear_console()
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
    print("[","Введите любой символ, чтобы выйти в главное меню".center(50),"]")
    print("[","".center(50, "-"),"]")
    d = input("> ")
    return "Выход из функции"


#Функция "Главное меню"
def starting_point():
    current_time = strftime("%d.%m.%Y в %H:%M:%S", localtime())
    print("Формат дат: День.Месяц.Год")
    print("Документ создан         06.08.2025 в 13:59:22")
    print("Документ завершен       00.00.0000 в 00:00:00")
    print("Документ открыт        ", current_time)
    
    with open("Даты изменения Справочника.txt","a") as change_date_file:
        change_date_file.write(f"{current_time}\n")
        print("Текущая дата открытия файла успешно записана в текстовый файл 'Даты изменения Справочника'\n")
    print(
        "Добро пожаловать в справочник. Выберите раздел, который вы хотите прочитать:\n"
        +"[ 1 ] [ Арифметические операции ] [ Завершена 16.09.2025 в 19:19:43 ]\n"
        +"[ 2 ] [ Условные операторы      ] [ Завершена 16.09.2025 в 20:07:22 ]\n"
        +"[ 3 ] [ Циклы                   ] [ Завершена 16.09.2025 в 20:34:51 ]\n"
        +"[ 4 ] [ Массивы                 ] [ Завершена 17.09.2025 в 18:09:36 ]\n"
        +"[ 5 ] [ Матрицы                 ] [ Завершена 17.09.0025 в 18:51:56 ]\n"
        +"[ 6 ] [ ANSI Escape коды        ] [ Завершена 00.00.0000 в 00:00:00 ]\n"
        +"[ - ] [ Выход                   ] [ Любой ввод выходит из программы ]\n"
        )
    
    try:
        a = int(input("> "))
    except ValueError:
        return 0
    if a == 1:
        clear_console()
        arithmetic_operations()
    elif a == 2:
        clear_console()
        if_elses()
    elif a == 3:
        loops()
    elif a == 4:
        arrays()
    elif a == 5:
        matrix()
    elif a == 6:
        ansies()
    else:
        return 0

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.systen('clear')
    
starting_point()
