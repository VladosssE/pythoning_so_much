import os
from .arithmetic_operations import *
from .logging import log_check
from .display_time import simple_time


def log_path():
    logs_folder = "logs"
    os.makedirs(logs_folder, exist_ok=True)
    return logs_folder

def write_log(message, extra):
    result_message = log_check(message)
    main_file_path = os.path.join(log_path(), "Действия с проектом.md")

    if result_message == True:
        if os.path.exists(main_file_path):
            with open(main_file_path, "a", encoding="utf-8") as mo_file:
                mo_file.write(f"| {message} | {simple_time()} | {extra} |\n")
        else:
            with open(main_file_path, "a", encoding="utf-8") as mo_file:
                mo_file.write(
                              f"Откройте файл в Obsidian, либо другой программе, поддерживающей MarkDown, чтобы просмотреть таблицу\n"
                              +f"\n"
                              +f"| Состояние | Дата | Дополнительно |\n"
                              +f"| --- | --- | --- |\n"
                              +f"| {current_file} | {simple_time()} | {extra} |\n"
                              )
    else:
        return 0

def file_ao_write(a, b):
    ao_file_path = os.path.join(log_path(), "1 - Арифметические операции.md")

    if os.path.exists(ao_file_path):
        with open(ao_file_path, "a", encoding="utf-8") as ao_open_file:
            ao_open_file.write(f"| {simple_time()} | {a} | {b} | {plus(a, b)} | {minus(a, b)} | {multiply(a, b)} | {divide(a, b)} | {full_divide(a, b)} | {remainder(a, b)} |\n")
    else:
        with open(ao_file_path, "a", encoding="utf-8") as ao_open_file:
            ao_open_file.write(
                            f"Откройте файл в Obsidian, либо другой программе, поддерживающей MarkDown, чтобы просмотреть таблицу\n"
                            +f"\n"
                            +f"| Дата | Значение а | Значение b | Сложение | Вычитание | Умножение | Деление | Ц. Деление | Остаток |\n"
                            +f"| --- | --- | --- | --- | --- | --- | --- | --- | --- |\n"
                            +f"| {simple_time()} | {a} | {b} | {plus(a, b)} | {minus(a, b)} | {multiply(a, b)} | {divide(a, b)} | {full_divide(a, b)} | {remainder(a, b)} |\n"
                            )
    return 0

def file_square_root_write(formula, D, result):
    sr_file_path = os.path.join(log_path(), "2 - Квадратный уравнение.md")

    if os.path.exists(sr_file_path):
        with open(sr_file_path, "a", encoding="utf-8") as sr_open_file:
            sr_open_file.write(f"| {simple_time()} | {formula} | {D} | {result} |\n")
    else:
        with open(sr_file_path, "a", encoding="utf-8") as sr_open_file:
            sr_open_file.write(
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
        with open(fact_file_path, "a", encoding="utf-8") as fa_open_file:
            fa_open_file.write(f"| {simple_time()} | {num} | {factorial} |\n")
    else:
        with open(fact_file_path, "a", encoding="utf-8") as fa_open_file:
            fa_open_file.write(
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
        with open(array_file_path, "a", encoding="utf-8") as ar_open_file:
            ar_open_file.write(f"| {simple_time()} | {Array} |\n")
    else:
        with open(array_file_path, "a", encoding="utf-8") as ar_open_file:
            ar_open_file.write(
                            f"Откройте файл в Obsidian, либо другой программе, поддерживающей MarkDown, чтобы просмотреть таблицу\n"
                            +f"\n"
                            +f"| Дата | Массив |\n"
                            +f"| --- | --- |\n"
                            +f"| {simple_time()} | {Array} |\n"
                            )
    return 0
