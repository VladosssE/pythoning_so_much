import os
import code
from functions import *

log_create()
error_log_create()

def starting_point():
    write_log("В главном меню", "Нет")
    display_main()
    a = input("> ")
    if a == "1" or a == "Арифметические операции":
        clear_console()
        write_log("Открыта функция Арифметические операции", "Нет")
        display_arithmetic()
        display_arithmetic_action()
        b = input("> ")
        if b == "1" or b == "Сложение":
            a, b = display_arithmetic_input()
            op, er_message, result = display_arithmetic_plus(a, b)
            file_ao_write(a, b, er_message, operations=[op])
            write_log("Использована функция Арифметические операции (Сложение)", "Нет")
            finish = input("Любой ввод вернет в главное меню > ")
            
        elif b == "2" or b == "Вычитание":
            a, b = display_arithmetic_input()
            op, er_message, result = display_arithmetic_minus(a, b)
            file_ao_write(a, b, er_message, operations=[op])
            write_log("Использована функция Арифметические операции (Вычитание)", "Нет")
            finish = input("Любой ввод вернет в главное меню > ")
            
        elif b == "3" or b == "Умножение":
            a, b = display_arithmetic_input()
            op, er_message, result = display_arithmetic_multiply(a, b)
            file_ao_write(a, b, er_message, operations=[op])
            write_log("Использована функция Арифметические операции (Умножение)", "Нет")
            finish = input("Любой ввод вернет в главное меню > ")
            
        elif b == "4" or b == "Деление":
            a, b = display_arithmetic_input()
            op, er_message, result = display_arithmetic_divide(a, b)
            file_ao_write(a, b, er_message, operations=[op])
            write_log("Использована функция Арифметические операции (Деление)", "Нет")
            finish = input("Любой ввод вернет в главное меню > ")
            
        elif b == "5" or b == "Целочисленное деление":
            a, b = display_arithmetic_input()
            op, er_message, result = display_arithmetic_full_divide(a, b)
            file_ao_write(a, b, er_message, operations=[op])
            write_log("Использована функция Арифметические операции (Целочисленное деление)", "Нет")
            finish = input("Любой ввод вернет в главное меню > ")
            
        elif b == "6" or b == "Остаток":
            a, b = display_arithmetic_input()
            op, er_message, result = display_arithmetic_remainder(a, b)
            file_ao_write(a, b, er_message, operations=[op])
            write_log("Использована функция Арифметические операции (Остаток)", "Нет")
            finish = input("Любой ввод вернет в главное меню > ")
            
        else:
            return starting_point()
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

    elif a == "5" or a == "Матрицы":
        clear_console()
        write_log("Открыта функция Матрицы", "Нет")
        display_matrix()
        Matrix = display_matrix_input()
        display_matrix_math(Matrix)
        write_log("Использована функция Матрицы", "Нет")
        file_matrix_write(Matrix)
        finish = input("Любой ввод вернет в главное меню > ")
        return clear_console(), starting_point()

    elif a == "6" or a == "Сумма матриц":
        clear_console()
        write_log("Открыта функция Сумма матриц", "Нет")
        display_sum_matrix()
        Matrix, Matrix2, summed_matrix = display_sum_matrix_input()
        display_sum_matrix_math(Matrix, Matrix2, summed_matrix)
        write_log("Использована функция Сумма матриц", "Нет")
        file_sum_matrix_write(Matrix, Matrix2, summed_matrix)
        finish = input("Любой ввод вернет в главное меню > ")
        return clear_console(), starting_point()

    elif a == "7" or a == "Шифр Цезаря (ASCII)":
        clear_console()
        write_log("Открыта функция Шифр Цезаря (ASCII)", "Нет")
        display_caesar_ascii()
        start_string, bias, result = display_caesar_ascii_input()
        display_caesar_ascii_math(start_string, bias, result)
        write_log("Использована функция Шифр Цезаря (ASCII)", "Нет")
        file_caesar_ascii_write(start_string, bias, result)
        finish = input("Любой ввод вернет в главное меню > ")
        return clear_console(), starting_point()

    elif a == "8" or a == "Шифр Цезаря (Словарь)":
        clear_console()
        write_log("Открыта функция Шифр Цезаря (Словарь)", "Нет")
        display_caesar_dictionary()
        text, shift, result = display_caesar_dictionary_input()
        display_caesar_dictionary_math(text, shift, result)
        write_log("Использована функция Шифр Цезаря (Словарь)", "Нет")
        file_caesar_dictionary_write(text, shift, result)
        finish = input("Любой ввод вернет в главное меню > ")
        return clear_console(), starting_point()
    
    elif a == "x" or a == "Настройки логирования":
        clear_console()
        write_log("Открыта функция Настройки логирования", "Нет")
        display_log_settings()
        log_read()
        finish = input("Любой ввод вернет в главное меню > ")
        write_log("Использована функция Настройки логирования", "Нет")
        return clear_console(), starting_point()

    elif a == "y" or a == "ANSI Escape коды":
        clear_console()
        write_log("Открыта функция ANSI Escape коды", "Нет")
        display_ansi_escape_codes()
        finish = input("Любой ввод вернет в главное меню > ")
        write_log("Использована функция ANSI Escape коды", "Нет")
        return clear_console(), starting_point()

    elif a == "z" or a == "Настройки ошибок":
        clear_console()
        write_log("Открыта функция Настройки ошибок", "Нет")
        display_error_log_settings()
        error_log_read()
        finish = input("Любой ввод вернет в главное меню > ")
        write_log("Использована функция Настройки ошибок", "Нет")
        return clear_console(), starting_point()

    elif a == "a" or a == "Протестировать функцию Арифметические операции":
        clear_console()
        write_log("Открыта функция Тестирование функций (Арифметические операции)", "Нет")
        display_testing_arithmetic()
        display_testing_arithmetic_math()
        finish = input("Любой ввод вернет в главное меню > ")
        write_log("Использована функция Тестирование функций", "Нет")
        return clear_console(), starting_point()

    elif a == "b" or a == "Протестировать функцию Квадратное уравнение":
        clear_console()
        write_log("Открыта функция Тестирование функций (Квадратное уравнение)", "Нет")
        display_testing_square_root()
        display_testing_square_root_math()
        finish = input("Любой ввод вернет в главное меню > ")
        write_log("Использована функция Тестирование функций", "Нет")
        return clear_console(), starting_point()

    elif a == "c" or a == "Протестировать функцию Факториал":
        clear_console()
        write_log("Открыта функция Тестирование функций (Факториал)", "Нет")
        display_testing_factorial()
        display_testing_factorial_math()
        finish = input("Любой ввод вернет в главное меню > ")
        write_log("Использована функция Тестирование функций", "Нет")
        return clear_console(), starting_point()

    elif a == "d" or a == "Протестировать функцию Массивы":
        clear_console()
        write_log("Открыта функция Тестирование функций (Массивы)", "Нет")
        display_testing_array()
        display_testing_array_math()
        finish = input("Любой ввод вернет в главное меню > ")
        write_log("Использована функция Тестирование функций", "Нет")
        return clear_console(), starting_point()

    elif a == "e" or a == "Протестировать функцию Матрицы":
        clear_console()
        write_log("Открыта функция Тестирование функций (Матрицы)", "Нет")
        display_testing_matrix()
        display_testing_matrix_math()
        finish = input("Любой ввод вернет в главное меню > ")
        write_log("Использована функция Тестирование функций", "Нет")
        return clear_console(), starting_point()

    elif a == "f" or a == "Протестировать функцию Сумма матриц":
        clear_console()
        write_log("Открыта функция Тестирование функций (Сумма матриц)", "Нет")
        display_testing_sum_matrix()
        display_testing_sum_matrix_math()
        finish = input("Любой ввод вернет в главное меню > ")
        write_log("Использована функция Тестирование функций", "Нет")
        return clear_console(), starting_point()

    elif a == "g" or a == "Протестировать функцию Шифр Цезаря (ASCII)":
        clear_console()
        write_log("Открыта функция Тестирование функций (Шифр Цезаря (ASCII))", "Нет")
        display_testing_caesar_ascii()
        display_testing_caesar_ascii_math()
        finish = input("Любой ввод вернет в главное меню > ")
        write_log("Использована функция Тестирование функций", "Нет")
        return clear_console(), starting_point()

    elif a == "h" or a == "Протестировать функцию Шифр Цезаря (Словарь)":
        clear_console()
        write_log("Открыта функция Тестирование функций (Шифр Цезаря (Словарь))", "Нет")
        display_testing_caesar_dictionary()
        display_testing_caesar_dictionary_math()
        finish = input("Любой ввод вернет в главное меню > ")
        write_log("Использована функция Тестирование функций", "Нет")
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
