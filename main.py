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
        a, b = display_arithmetic_input()
        display_arithmetic_math(a, b)
        write_log("Использована функция Арифметические операции", "Нет")
        file_ao_write(a, b)
        finish = input("Любой ввод вернет в главное меню > ") # Пауза
        return clear_console(), starting_point()

    elif a == "2" or a == "Квадратное уравнение":
        clear_console()
        write_log("Открыта функция Квадратное уравнение", "Нет")
        display_square_root()
        formula, D, result = display_square_root_input()
        display_square_root_math(formula, D, result)
        write_log("Использована функция Квадратное уравнение", "Нет")
        file_square_root_write(formula, D, result)
        finish = input("Любой ввод вернет в главное меню > ")
        return clear_console(), starting_point()

    elif a == "3" or a == "Факториал":
        clear_console()
        write_log("Открыта функция Факториал", "Нет")
        display_factorial()
        num, factorial = display_factorial_input()
        display_factorial_math(num, factorial)  
        write_log("Использована функция Факториал", "Нет")
        file_factorial_write(num, factorial)
        finish = input("Любой ввод вернет в главное меню > ")
        return clear_console(), starting_point()

    elif a == "4" or a == "Массивы":
        clear_console()
        write_log("Открыта функция Массивы", "Нет")
        display_array()
        Array, width = display_array_input()
        display_array_math(Array)
        write_log("Использована функция Массивы", "Нет")
        file_array_write(Array)
        array_actions(Array, width)
        
    elif a == "0" or a == "Настройки логирования":
        write_log("Открыта функция Настройки логирования", "Нет")
        clear_console()
        display_log_settings()
        log_read()
        finish = input("Любой ввод вернет в главное меню > ")
        write_log("Использована функция Настройки логирования", "Нет")
        return clear_console(), starting_point()
    else:
        return 0

def array_actions(Array, width):
    display_array_actions()
    action = input("> ")
    if action == "1" or action == "Поиск по массиву":
        display_array_item_find(Array, width)
        write_log("Массивы: Поиск по массиву", "Нет")
        file_array_write(Array)
        finish = input("Продолжить? 1/0 > ")
        if finish == "1":
            array_actions(Array, width)
        else:
            starting_point()
            
    elif action == "2" or action == "Добавление элементов":
        display_array_item_add(Array, width)
        write_log("Массивы: Добавление элементов", "Нет")
        file_array_write(Array)
        finish = input("Продолжить? 1/0 > ")
        if finish == "1":
            return array_actions(Array, width)
        else:
            return starting_point()
            
    elif action == "3" or action == "Изменение элементов":
        display_array_item_change(Array, width)
        write_log("Массивы: Изменение элементов", "Нет")
        file_array_write(Array)
        finish = input("Продолжить? 1/0 > ")
        if finish == "1":
            return array_actions(Array, width)
        else:
            return starting_point()

    elif action == "4" or action == "Удаление элементов":
        display_array_item_delete(Array, width)
        write_log("Массивы: Удаление элементов", "Нет")
        file_array_write(Array)
        finish = input("Продолжить? 1/0 > ")
        if finish == "1":
            return array_actions(Array, width)
        else:
            return starting_point()

    else:
        starting_point()
        write_log("Выход из программы", "Нет")
            
starting_point()
