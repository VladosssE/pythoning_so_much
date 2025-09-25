import os

from functions import *

def starting_point():
    file_main("В главном меню", "Нет")
    print("[","".center(50, "-"),"]\n"
          +"[","Документ создан","  ]","[","06 Август 2025 13:59:22".center(28),"]\n"
          +"[","Документ завершен","]","[","00.00.0000 00:00:00".center(28),"]\n"
          +"[","Документ открыт","  ]","[", simple_time().center(28),"]\n"
          +"[","".center(50, "-"),"]\n"
          +"[ Выберите раздел, который вы хотите прочитать:      ]\n"
          +"[ 1 ] [ Арифметические операции                      ]\n"
          +"[ 2 ] [ Квадратное уравнение                         ]\n"
          +"[ 3 ] [ Факториал                                    ]\n"
          +"[ 4 ] [ Массивы                                      ]\n"
         )
    a = input("> ")
    if a == "1" or a == "Арифметические операции":
        clear_console()
        file_main("Открыта функция Арифметические операции", "Нет")
        print("[","ВЫБРАНО: Арифметические операции".center(50),"]")
        print("[ Выводит результаты базовых арифметических операций ]\n")
        try:
            a = float(input("Введите значение a: "))
            b = float(input("Введите значение b: "))
        except ValueError:
            print("\u001b[31m\n[","Ошибка: Введено не числовое значение".center(50),"]\u001b[0m")
            file_main("Арифметические операции: ValueError", "Ошибка: Введено не числовое значение")
            finish = input("Любой ввод вернет в главное меню > ") # Пауза
            return clear_console(), starting_point()
        
        plus_v = plus(a, b)
        minus_v = minus(a, b)
        mult = multiply(a, b)
        div = divide(a, b)
        fdiv = full_divide(a, b)
        rem = remainder(a, b)

        print(
            f"Сложение:              {a} + {b}  = {plus_v}\n"
            +f"Вычитание:             {a} - {b}  = {minus_v}\n"
            +f"Умножение:             {a} * {b}  = {mult}\n"
            +f"Деление:               {a} / {b}  = {div}\n"
            +f"Целочисленное деление: {a} // {b} = {fdiv}\n"
            +f"Нахождение остатка:    {a} % {b}  = {rem}\n"
            )
        file_main("Использована функция Арифметические операции", "Нет")
        file_ao(a, b, plus_v, minus_v, mult, div, fdiv, rem)
        finish = input("Любой ввод вернет в главное меню > ")
        return clear_console(), starting_point()

    elif a == "2" or a == "Квадратное уравнение":
        clear_console()
        file_main("Открыта функция Квадратное уравнение", "Нет")
        print("[","ВЫБРАНО: Квадратное уравнение".center(50),"]")
        print("[","Решает полное квадратное уравнение".center(50),"]\n")
        try:
            a = int(input("Введите значение a: "))
            b = int(input("Введите значение b: "))
            c = int(input("Введите значение c: "))
        except ValueError:
            file_main("Квадратное уравнение: ValueError", "Ошибка: Введено не числовое значение")
            print("\033[31m\n[ Ошибка: Введено не числовое значение ]\033[0m")
            finish = input("Любой ввод вернет в главное меню > ")
            return clear_console(), starting_point()
        print()
        formula = square_root_formula(a, b, c)
        D = discriminant(a, b, c)
        result = square_root_mathing(a, b, c, D)
        print("Формула:",formula)
        print("Дискриминант:",D)
        print("Ответ:",result,"\n")

        file_main("Использована функция Квадратное уравнение", "Нет")
        file_square_root(formula, D, result)
        finish = input("Любой ввод вернет в главное меню > ")
        return clear_console(), starting_point()

    elif a == "3" or a == "Факториал":
        clear_console()
        file_main("Открыта функция Факториал", "Нет")
        print("[","ВЫБРАНО: Факториал".center(50),"]")
        print("[","Выводит факториал числа".center(50),"]")
                           
        try:
            num = int(input("Введите число: "))
        except ValueError:
            print("\033[31m\n[ Ошибка: Введено не числовое значение ]\033[0m")
            file_main("Квадратное уравнение: ValueError", "Ошибка: Введено не числовое значение")
            finish = input("Любой ввод вернет в главное меню > ")
            return clear_console(), starting_point()

        factorial = fact(num)
        print(f"Введено значение = {num}")
        print(f"Факториал равен = {factorial}\n")

        file_main("Использована функция Факториал", "Нет")
        file_factorial(num, factorial)
        finish = input("Любой ввод вернет в главное меню > ")
        return clear_console(), starting_point()

    elif a == "4" or a == "Массивы":
        clear_console()
        file_main("Открыта функция Массивы", "Нет")
        print("[","ВЫБРАНО: Массивы".center(50),"]")
        print("[","Выводит простой массив из введенных значений".center(50),"]")
        print("[","Пример: ['0', '1', '2']".center(50),"]\n")

        try:
            width = int(input("Введите количество элементов в массиве: "))
        except ValueError:
            print("\033[31m\n[ Ошибка: Введено не числовое значение ]\033[0m")
            file_main("Массив: ValueError", "Ошибка: Введено не числовое значение")
            return starting_point()
        Array = array_create(width)
        print(f"Массив = {Array}")
        print()

        file_main("Использована функция Массивы", "Нет")
        file_array(Array)
        array_actions(Array, width)
    else:
        return 0

def array_actions(Array, width):
    print(
         "[","Действия с массивом:".center(50),"]\n"
         +"[ 1 ] [","Поиск по массиву","                            ]\n"
         +"[ 2 ] [","Добавление элементов","                        ]\n"
         +"[ 3 ] [","Изменение элементов","                         ]\n"
         +"[ 4 ] [","Удаление элементов","                          ]\n"
         +"[ 5 ] [","Выход","                                       ]\n"
         )
    action = input("> ")
    if action == "1" or action == "Поиск по массиву":
        print(f"Текущий массив: {Array}")
        target = input("Что вы хотите найти? > ")
        print(array_find(Array, target))
        file_main("Массивы: Поиск по массиву", "Нет")
        file_array(Array)
        finish = input("Продолжить? 1/0 > ")
        if finish == "1":
            array_actions(Array, width)
        else:
            starting_point()
            
    elif action == "2" or action == "Добавление элементов":
        print(f"Текущий массив: {Array}")
        try:
            add = input("Какой элемент хотите добавить? > ")
            pos = int(input("В какую позицию хотите добавить? > "))
        except ValueError:
            print("\033[31m\n[ Ошибка: Введено недопустимое значение ]\033[0m")
            file_main("Массивы: Добавление элементов: ValueError", "Ошибка: Введено недопустимое значение")
            return array_actions(Array, width)
        print(array_add(Array, add, pos))
        file_main("Массивы: Добавление элементов", "Нет")
        file_array(Array)
        finish = input("Продолжить? 1/0 > ")
        if finish == "1":
            return array_actions(Array, width)
        else:
            return starting_point()
            
    elif action == "3" or action == "Изменение элементов":
        print(f"Текущий массив: {Array}")
        try:
            pos = int(input("В какой позиции хотите изменить значение? > "))
            change = input("Новое значение > ")
        except ValueError:
            print("\033[31m\n[ Ошибка: Введено недопустимое значение ]\033[0m")
            file_main("Массивы: Изменение элементов: ValueError", "Ошибка: Введено недопустимое значение")
            return array_actions(Array, width)
        print(array_change(Array, change, pos, width))
        file_main("Массивы: Изменение элементов", "Нет")
        file_array(Array)
        finish = input("Продолжить? 1/0 > ")
        if finish == "1":
            return array_actions(Array, width)
        else:
            return starting_point()

    elif action == "4" or action == "Удаление элементов":
        print(f"Текущий массив: {Array}")
        delete = input("Какой элемент вы хотите удалить? > ")
        print(array_delete(Array, delete, width))
        file_main("Массивы: Удаление элементов", "Нет")
        file_array(Array)
        finish = input("Продолжить? 1/0 > ")
        if finish == "1":
            return array_actions(Array, width)
        else:
            return starting_point()

    else:
        starting_point()
        file_main("Выход из программы", "Нет")
            
starting_point()
