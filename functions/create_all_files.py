import os
from functions.display_time import simple_time
from functions.logging import log_check

def log_path():
    logs_folder = "logs"
    os.makedirs(logs_folder, exist_ok=True)
    return logs_folder

def write_log(message, extra):
    result_message = log_check(message)
    main_file_path = os.path.join(log_path(), "Действия с проектом.md")

    if result_message == True:
        if os.path.exists(main_file_path):
            with open(main_file_path, "a", encoding="utf-8") as file:
                file.write(f"| {simple_time()} | {message} | {extra} |\n")
        else:
            with open(main_file_path, "a", encoding="utf-8") as file:
                file.write(
                              f"Откройте файл в Obsidian, либо другой программе, поддерживающей MarkDown, чтобы просмотреть таблицу\n"
                              +f"\n"
                              +f"| Дата | Состояние | Дополнительно |\n"
                              +f"| --- | --- | --- |\n"
                              +f"| {simple_time()} | Файл создан | Первое открытие проекта |\n"
                              )
    else:
        return 0

def file_ao_write(a, b, operation, er_message, result):
    from .arithmetic_operations import plus, minus, multiply, divide, full_divide, remainder
    ao_file_path = os.path.join(log_path(), "1 - Арифметические операции.md")
    
    if os.path.exists(ao_file_path):
        with open(ao_file_path, "a", encoding="utf-8") as file:
            file.write(f"| {simple_time()} | {operation} | {er_message} | {a} | {b} | {result} |\n")
    else:
        with open(ao_file_path, "a", encoding="utf-8") as file:
            file.write(
                        f"Откройте файл в Obsidian, либо другой программе, поддерживающей MarkDown, чтобы просмотреть таблицу\n"
                        +f"\n"
                        +f"| Дата | Выбрано | Состояние | Значение а | Значение b | Результат |\n"
                        +f"| --- | --- | --- | --- | --- | --- |\n"
                        +f"| {simple_time()} | {operation} | {er_message} | {a} | {b} | {result} |\n"
                        )
    return "Успешно"

def file_square_root_write(er_message, formula, D, x1, x2):
    sr_file_path = os.path.join(log_path(), "2 - Квадратное уравнение.md")

    if os.path.exists(sr_file_path):
        with open(sr_file_path, "a", encoding="utf-8") as file:
            file.write(f"| {simple_time()} | {er_message} | {formula} | {D} | {x1} | {x2} |\n")
    else:
        with open(sr_file_path, "a", encoding="utf-8") as file:
            file.write(
                            f"Откройте файл в Obsidian, либо другой программе, поддерживающей MarkDown, чтобы просмотреть таблицу\n"
                            +f"\n"
                            +f"| Дата | Состояние | Формула | Дискриминант | Первый корень | Второй корень |\n"
                            +f"| --- | --- | --- | --- | --- | --- |\n"
                            +f"| {simple_time()} | {er_message} | {formula} | {D} | {x1} | {x2} |\n"
                            )
    return 0


def file_factorial_write(num, er_message, factorial):
    fact_file_path = os.path.join(log_path(), "3 - Факториал.md")

    if os.path.exists(fact_file_path):
        with open(fact_file_path, "a", encoding="utf-8") as file:
            file.write(f"| {simple_time()} | {er_message} | {num} | {factorial} |\n")
    else:
        with open(fact_file_path, "a", encoding="utf-8") as file:
            file.write(
                            f"Откройте файл в Obsidian, либо другой программе, поддерживающей MarkDown, чтобы просмотреть таблицу\n"
                            +f"\n"
                            +f"| Дата | Состояние | Значение | Факториал |\n"
                            +f"| --- | --- | --- | --- |\n"
                            +f"| {simple_time()} | {er_message} | {num} | {factorial} |\n"
                            )
    return 0


def file_array_write(er_message, Array):
    array_file_path = os.path.join(log_path(), "4 - Массивы.md")

    if os.path.exists(array_file_path):
        with open(array_file_path, "a", encoding="utf-8") as file:
            file.write(f"| {simple_time()} | {er_message} | {Array} |\n")
    else:
        with open(array_file_path, "a", encoding="utf-8") as file:
            file.write(
                            f"Откройте файл в Obsidian, либо другой программе, поддерживающей MarkDown, чтобы просмотреть таблицу\n"
                            +f"\n"
                            +f"| Дата | Состояние | Массив |\n"
                            +f"| --- | --- | --- |\n"
                            +f"| {simple_time()} | {er_message} | {Array} |\n"
                            )
    return 0


def file_matrix_write(er_message, Matrix):
    matrix_file_path = os.path.join(log_path(), "5 - Матрицы.md")

    if os.path.exists(matrix_file_path):
        with open (matrix_file_path, "a", encoding="utf-8") as file:
            file.write(f"| {simple_time()} | {er_message} | {Matrix} |\n")
    else:
        with open(matrix_file_path, "a", encoding="utf-8") as file:
            file.write(
                            f"Откройте файл в Obsidian, либо другой программе, поддерживающей MarkDown, чтобы просмотреть таблицу\n"
                            +f"\n"
                            +f"| Дата | Состояние | Матрица |\n"
                            +f"| --- | --- | --- |\n"
                            +f"| {simple_time()} | {er_message} | {Matrix} |\n"
                            )
    return 0


def file_sum_matrix_write(er_message, Matrix, Matrix2, summed_matrix):
    sum_matrix_file_path = os.path.join(log_path(), "6 - Сумма матриц.md")

    if os.path.exists(sum_matrix_file_path):
        with open (sum_matrix_file_path, "a", encoding="utf-8") as file:
            file.write(f"| {simple_time()} | {er_message} | {Matrix} | {Matrix2} | {summed_matrix} |\n")
    else:
        with open(sum_matrix_file_path, "a", encoding="utf-8") as file:
            file.write(
                            f"Откройте файл в Obsidian, либо другой программе, поддерживающей MarkDown, чтобы просмотреть таблицу\n"
                            +f"\n"
                            +f"| Дата | Состояние | Первая матрица | Вторая матрица | Сумма матриц |\n"
                            +f"| --- | --- | --- | --- | --- |\n"
                            +f"| {simple_time()} | {er_message} | {Matrix} | {Matrix2} | {summed_matrix} |\n"
                            )
    return 0


def file_caesar_ascii_write(start_string, bias, er_message, result):
    caesar_ascii_file_path = os.path.join(log_path(), "7 - Шифр Цезаря (ASCII).md")

    if os.path.exists(caesar_ascii_file_path):
        with open(caesar_ascii_file_path, "a", encoding="utf-8") as file:
            file.write(f"| {simple_time()} | {er_message} | {start_string} | {bias} | {result} |\n")
    else:
        with open(caesar_ascii_file_path, "a", encoding="utf-8") as file:
            file.write(
                            f"Откройте файл в Obsidian, либо другой программе, поддерживающей MarkDown, чтобы просмотреть таблицу\n"
                            +f"\n"
                            +f"| Дата | Состояние | Первичная строка | Смещение | Зашифрованная строка |\n"
                            +f"| --- | --- | --- | --- | --- |\n"
                            +f"| {simple_time()} | {er_message} | {start_string} | {bias} | {result} |\n"
                            )
    return 0


def file_caesar_dictionary_write(text, shift, er_message, result):
    caesar_dictionary_file_path = os.path.join(log_path(), "8 - Шифр Цезаря (Словарь).md")

    if os.path.exists(caesar_dictionary_file_path):
        with open(caesar_dictionary_file_path, "a", encoding="utf-8") as file:
            file.write(f"| {simple_time()} | {er_message} | {text} | {shift} | {result}\n")
    else:
        with open(caesar_dictionary_file_path, "a", encoding="utf-8") as file:
            file.write(
                            f"Откройте файл в Obsidian, либо другой программе, поддерживающей MarkDown, чтобы просмотреть таблицу\n"
                            +f"\n"
                            +f"| Дата | Состояние | Первичная строка | Смещение | Зашифрованная строка |\n"
                            +f"| --- | --- | --- | --- | --- |\n"
                            +f"| {simple_time()} | {er_message} | {text} | {shift} | {result} |\n"
                            )
    return 0
