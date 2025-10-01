from .create_all_files import *
def plus(a, b):
    operation = "Сложение"
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        write_log("Арифметические операции (Сложение): ValueError", "Ошибка: Введено не числовое значение")
        er_message = "Введено недопустимое значение"
        result = "-"
    else:
        er_message = "Успешно"
        result = round(a+b, 2)
    return operation, er_message, result


def minus(a, b):
    operation = "Вычитание"
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        write_log("Арифметические операции (Вычитание): ValueError", "Ошибка: Введено не числовое значение")
        er_message = "Введено недопустимое значение"
        result = "-"
    else:
        er_message = "Успешно"
        result = round(a-b, 2)
    return operation, er_message, result


def divide(a, b):
    operation = "Деление"
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        write_log("Арифметические операции (Деление): ValueError", "Ошибка: Введено не числовое значение")
        er_message = "Введено недопустимое значение"
        result = "-"
    else:
        try: a/b or b/a
        except ZeroDivisionError:
            write_log("Арифметические операции (Деление): ZeroDivisionError", "")
            er_message = "На ноль делить нельзя"
            result = "-"
        else:
            er_message = "Успешно"
            result = round(a/b, 2)
    return operation, er_message, result


def full_divide(a, b):
    operation = "Целочисленное деление"
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        write_log("Арифметические операции (Целочисленное деление): ValueError", "Ошибка: Введено не числовое значение")
        er_message = "Введено недопустимое значение"
        result = "-"
    else:
        try: a//b or b//a
        except ZeroDivisionError:
            write_log("Арифметические операции (Целочисленное деление): ZeroDivisionError", "Внимание: На ноль делить нельзя")
            er_message = "На ноль делить нельзя"
            result = "-"
        else:
            er_message = "Успешно"
            result = round(a//b, 2)
    return operation, er_message, result


def multiply(a, b):
    operation = "Умножение"
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        write_log("Арифметические операции (Умножение): ValueError", "Ошибка: Введено не числовое значение")
        er_message = "Введено недопустимое значение"
        result = "-"
    else:
        er_message = "Успешно"
        result = round(a*b, 2)
    return operation, er_message, result


def remainder(a, b):
    operation = "Нахождение остатка"
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        write_log("Арифметические операции (Нахождение остатка): ValueError", "Ошибка: Введено не числовое значение")
        er_message = "Введено недопустимое значение"
        result = "-"
    else:
        try: a%b or b%a
        except ZeroDivisionError:
            write_log("Арифметические операции (Нахождение остатка): ZeroDivisionError", "Внимание: Остатка от нуля не существует")
            er_message = "Остатка от нуля не существует"
            result = "-"
        else:
            er_message = "Успешно"
            result = round(a%b, 2)
    return operation, er_message, result
