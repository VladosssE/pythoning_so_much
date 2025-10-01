import os
from .display_time import simple_time
from .logging import log_check

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

def file_square_root_write(formula, D, result):
    sr_file_path = os.path.join(log_path(), "2 - Квадратный уравнение.md")

    if os.path.exists(sr_file_path):
        with open(sr_file_path, "a", encoding="utf-8") as file:
            file.write(f"| {simple_time()} | {formula} | {D} | {result} |\n")
    else:
        with open(sr_file_path, "a", encoding="utf-8") as file:
            file.write(
                            f"Откройте файл в Obsidian, либо другой программе, поддерживающей MarkDown, чтобы просмотреть таблицу\n"
                            +f"\n"
                            +f"| Дата | Формула | Дискриминант | Ответ |\n"
                            +f"| --- | --- | --- | --- |\n"
                            +f"| {simple_time()} | {formula} | {D} | {result} |\n"
                            )
    return 0


def file_factorial_write(num, factorial):
    fact_file_path = os.path.join(log_path(), "3 - Факториал.md")

    if os.path.exists(fact_file_path):
        with open(fact_file_path, "a", encoding="utf-8") as file:
            file.write(f"| {simple_time()} | {num} | {factorial} |\n")
    else:
        with open(fact_file_path, "a", encoding="utf-8") as file:
            file.write(
                            f"Откройте файл в Obsidian, либо другой программе, поддерживающей MarkDown, чтобы просмотреть таблицу\n"
                            +f"\n"
                            +f"| Дата | Значение | Факториал |\n"
                            +f"| --- | --- | --- |\n"
                            +f"| {simple_time()} | {num} | {factorial} |\n"
                            )
    return 0


def file_array_write(Array):
    array_file_path = os.path.join(log_path(), "4 - Массивы.md")

    if os.path.exists(array_file_path):
        with open(array_file_path, "a", encoding="utf-8") as file:
            file.write(f"| {simple_time()} | {Array} |\n")
    else:
        with open(array_file_path, "a", encoding="utf-8") as file:
            file.write(
                            f"Откройте файл в Obsidian, либо другой программе, поддерживающей MarkDown, чтобы просмотреть таблицу\n"
                            +f"\n"
                            +f"| Дата | Массив |\n"
                            +f"| --- | --- |\n"
                            +f"| {simple_time()} | {Array} |\n"
                            )
    return 0


def file_matrix_write(Matrix):
    matrix_file_path = os.path.join(log_path(), "5 - Матрицы.md")

    if os.path.exists(matrix_file_path):
        with open (matrix_file_path, "a", encoding="utf-8") as file:
            file.write(f"| {simple_time()} | {Matrix} |\n")
    else:
        with open(matrix_file_path, "a", encoding="utf-8") as file:
            file.write(
                            f"Откройте файл в Obsidian, либо другой программе, поддерживающей MarkDown, чтобы просмотреть таблицу\n"
                            +f"\n"
                            +f"| Дата | Матрица |\n"
                            +f"| --- | --- |\n"
                            +f"| {simple_time()} | {Matrix} |\n"
                            )
    return 0


def file_sum_matrix_write(Matrix, Matrix2, summed_matrix):
    sum_matrix_file_path = os.path.join(log_path(), "6 - Сумма матриц.md")

    if os.path.exists(sum_matrix_file_path):
        with open (sum_matrix_file_path, "a", encoding="utf-8") as file:
            file.write(f"| {simple_time()} | {Matrix} | {Matrix2} | {summed_matrix} |\n")
    else:
        with open(sum_matrix_file_path, "a", encoding="utf-8") as file:
            file.write(
                            f"Откройте файл в Obsidian, либо другой программе, поддерживающей MarkDown, чтобы просмотреть таблицу\n"
                            +f"\n"
                            +f"| Дата | Первая матрица | Вторая матрица | Сумма матриц |\n"
                            +f"| --- | --- | --- | --- |\n"
                            +f"| {simple_time()} | {Matrix} | {Matrix2} | {summed_matrix} |\n"
                            )
    return 0


def file_caesar_ascii_write(start_string, bias, result):
    caesar_ascii_file_path = os.path.join(log_path(), "7 - Шифр Цезаря (ASCII).md")

    if os.path.exists(caesar_ascii_file_path):
        with open(caesar_ascii_file_path, "a", encoding="utf-8") as file:
            file.write(f"| {simple_time()} | {start_string} | {bias} | {result} |\n")
    else:
        with open(caesar_ascii_file_path, "a", encoding="utf-8") as file:
            file.write(
                            f"Откройте файл в Obsidian, либо другой программе, поддерживающей MarkDown, чтобы просмотреть таблицу\n"
                            +f"\n"
                            +f"| Дата | Первичная строка | Смещение | Зашифрованная строка |\n"
                            +f"| --- | --- | --- | --- |\n"
                            +f"| {simple_time()} | {start_string} | {bias} | {result} |\n"
                            )
    return 0


def file_caesar_dictionary_write(text, shift, result):
    caesar_dictionary_file_path = os.path.join(log_path(), "8 - Шифр Цезаря (Словарь).md")

    if os.path.exists(caesar_dictionary_file_path):
        with open(caesar_dictionary_file_path, "a", encoding="utf-8") as file:
            file.write(f"| {simple_time()} | {text} | {shift} | {result}\n")
    else:
        with open(caesar_dictionary_file_path, "a", encoding="utf-8") as file:
            file.write(
                            f"Откройте файл в Obsidian, либо другой программе, поддерживающей MarkDown, чтобы просмотреть таблицу\n"
                            +f"\n"
                            +f"| Дата | Первичная строка | Смещение | Зашифрованная строка |\n"
                            +f"| --- | --- | --- | --- |\n"
                            +f"| {simple_time()} | {text} | {shift} | {result} |\n"
                            )
    return 0
