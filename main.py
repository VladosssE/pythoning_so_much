import os

from functions import *

log_create()

def starting_point():
    write_log("В главном меню", "Нет")
    display_main()
    a = input("> ")
    if a == "1" or a == "Арифметические операции":
        clear_console()
        write_log("Открыта функция Арифметические операции", "Нет")
        display_arithmetic()
        try:
            a = float(input("Введите значение a: "))
            b = float(input("Введите значение b: "))
        except ValueError:
            print("\u001b[31m\n[","Ошибка: Введено не числовое значение".center(50),"]\u001b[0m")
            write_log("Арифметические операции: ValueError", "Ошибка: Введено не числовое значение")
            finish = input("Любой ввод вернет в главное меню > ") # Пауза
            return clear_console(), starting_point()
        
        display_arithmetic_math(a, b)
        write_log("Использована функция Арифметические операции", "Нет")
        file_ao(a, b)
        finish = input("Любой ввод вернет в главное меню > ")
        return clear_console(), starting_point()

    elif a == "2" or a == "Квадратное уравнение":
        clear_console()
        write_log("Открыта функция Квадратное уравнение", "Нет")
        display_square_root()
        try:
            a = int(input("Введите значение a: "))
            b = int(input("Введите значение b: "))
            c = int(input("Введите значение c: "))
        except ValueError:
            write_log("Квадратное уравнение: ValueError", "Ошибка: Введено не числовое значение")
            print("\033[31m\n[ Ошибка: Введено не числовое значение ]\033[0m")
            finish = input("Любой ввод вернет в главное меню > ")
            return clear_console(), starting_point()
        print()
        formula = square_root_formula(a, b, c)
        D = discriminant(a, b, c)
        result = square_root_mathing(a, b, c, D)
        display_square_root_math(formula, D, result)

        write_log("Использована функция Квадратное уравнение", "Нет")
        file_square_root(formula, D, result)
        finish = input("Любой ввод вернет в главное меню > ")
        return clear_console(), starting_point()

    elif a == "3" or a == "Факториал":
        clear_console()
        write_log("Открыта функция Факториал", "Нет")
        display_factorial()
        
        try:
            num = int(input("Введите число: "))
        except ValueError:
            print("\033[31m\n[ Ошибка: Введено не числовое значение ]\033[0m")
            write_log("Факториал: ValueError", "Ошибка: Введено не числовое значение")
            finish = input("Любой ввод вернет в главное меню > ")
            return clear_console(), starting_point()

        factorial = fact(num)
        display_factorial_math(num, factorial)
        write_log("Использована функция Факториал", "Нет")
        file_factorial(num, factorial)
        finish = input("Любой ввод вернет в главное меню > ")
        return clear_console(), starting_point()

    elif a == "4" or a == "Массивы":
        clear_console()
        write_log("Открыта функция Массивы", "Нет")
        display_array()

        try:
            width = int(input("Введите количество элементов в массиве: "))
        except ValueError:
            print("\033[31m\n[ Ошибка: Введено не числовое значение ]\033[0m")
            write_log("Массив: ValueError", "Ошибка: Введено не числовое значение")
            return starting_point()
        Array = array_create(width)
        display_array_math(Array)

        write_log("Использована функция Массивы", "Нет")
        file_array(Array)
        array_actions(Array, width)
        
    elif a == "0" or a == "Настройки логирования":
        clear_console()
        print("[","ВЫБРАНО: Настройки логирования".center(50),"]")
        print("[","Файл Действия с проектом сохраняет данные ниже".center(50),"]")
        print("[","Откройте ..saves/log_types.txt для изменения".center(50),"]")
        print(log_read())
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
        write_log("Массивы: Поиск по массиву", "Нет")
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
            write_log("Массивы: Добавление элементов: ValueError", "Ошибка: Введено недопустимое значение")
            return array_actions(Array, width)
        print(array_add(Array, add, pos))
        write_log("Массивы: Добавление элементов", "Нет")
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
            write_log("Массивы: Изменение элементов: ValueError", "Ошибка: Введено недопустимое значение")
            return array_actions(Array, width)
        print(array_change(Array, change, pos, width))
        write_log("Массивы: Изменение элементов", "Нет")
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
        write_log("Массивы: Удаление элементов", "Нет")
        file_array(Array)
        finish = input("Продолжить? 1/0 > ")
        if finish == "1":
            return array_actions(Array, width)
        else:
            return starting_point()

    else:
        starting_point()
        write_log("Выход из программы", "Нет")
            
starting_point()
