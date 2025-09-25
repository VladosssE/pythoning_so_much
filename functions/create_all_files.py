import os
from functions import display_time

def log_path():
    logs_folder = "logs"
    os.makedirs(logs_folder, exist_ok=True)
    return logs_folder


def file_main(current_file, extra):
    main_file_path = os.path.join(log_path(), "Действия с проектом.md")

    if os.path.exists(main_file_path):
        with open(main_file_path, "a", encoding="utf-8") as mo_file:
            mo_file.write(f"| {current_file} | {display_time} | {extra} |\n")
    else:
        with open(main_file_path, "a", encoding="utf-8") as mo_file:
            mo_file.write(
                          f"Откройте файл в Obsidian, либо другой программе, поддерживающей MarkDown, чтобы просмотреть таблицу\n"
                          +f"\n"
                          +f"| Состояние | Дата | Дополнительно |\n"
                          +f"| --- | --- | --- |\n"
                          +f"| {current_file} | {display_time} | {extra} |\n"
                          )
    return 0


def file_ao(a, b, plus_v, minus_v, mult, div, fdiv, rem):
    ao_file_path = os.path.join(log_path(), "1 - Арифметические операции.md")

    if os.path.exists(ao_file_path):
        with open(ao_file_path, "a", encoding="utf-8") as ao_open_file:
            ao_open_file.write(f"| {display_time} | {a} | {b} | {plus_v} | {minus_v} | {mult} | {div} | {fdiv} | {rem} |\n")
    else:
        with open(ao_file_path, "a", encoding="utf-8") as ao_open_file:
            ao_open_file.write(
                            f"Откройте файл в Obsidian, либо другой программе, поддерживающей MarkDown, чтобы просмотреть таблицу\n"
                            +f"\n"
                            +f"| Дата | Значение а | Значение b | Сложение | Вычитание | Умножение | Деление | Ц. Деление | Остаток |\n"
                            +f"| --- | --- | --- | --- | --- | --- | --- | --- | --- |\n"
                            +f"| {display_time} | {a} | {b} | {plus_v} | {minus_v} | {mult} | {div} | {fdiv} | {rem} |\n"
                            )
    return 0

def file_square_root(formula, D, result):
    sr_file_path = os.path.join(log_path(), "2 - Квадратный уравнение.md")

    if os.path.exists(sr_file_path):
        with open(sr_file_path, "a", encoding="utf-8") as sr_open_file:
            sr_open_file.write(f"| {display_time} | {formula} | {D} | {result} |\n")
    else:
        with open(sr_file_path, "a", encoding="utf-8") as sr_open_file:
            sr_open_file.write(
                            f"Откройте файл в Obsidian, либо другой программе, поддерживающей MarkDown, чтобы просмотреть таблицу\n"
                            +f"\n"
                            +f"| Дата | Формула | Дискриминант | Ответ |\n"
                            +f"| --- | --- | --- | --- |\n"
                            +f"| {display_time} | {formula} | {D} | {result} |\n"
                            )
    return 0


def file_factorial(num, factorial):
    fact_file_path = os.path.join(log_path(), "3 - Факториал.md")

    if os.path.exists(fact_file_path):
        with open(fact_file_path, "a", encoding="utf-8") as fa_open_file:
            fa_open_file.write(f"| {display_time} | {num} | {factorial} |\n")
    else:
        with open(fact_file_path, "a", encoding="utf-8") as fa_open_file:
            fa_open_file.write(
                            f"Откройте файл в Obsidian, либо другой программе, поддерживающей MarkDown, чтобы просмотреть таблицу\n"
                            +f"\n"
                            +f"| Дата | Значение | Факториал |\n"
                            +f"| --- | --- | --- |\n"
                            +f"| {display_time} | {num} | {factorial} |\n"
                            )
    return 0


def file_array(Array):
    array_file_path = os.path.join(log_path(), "4 - Массивы.md")

    if os.path.exists(array_file_path):
        with open(array_file_path, "a", encoding="utf-8") as ar_open_file:
            ar_open_file.write(f"| {display_time} | {Array} |\n")
    else:
        with open(array_file_path, "a", encoding="utf-8") as ar_open_file:
            ar_open_file.write(
                            f"Откройте файл в Obsidian, либо другой программе, поддерживающей MarkDown, чтобы просмотреть таблицу\n"
                            +f"\n"
                            +f"| Дата | Массив |\n"
                            +f"| --- | --- |\n"
                            +f"| {display_time} | {Array} |\n"
                            )
    return 0
