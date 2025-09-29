from .create_all_files import write_log
def plus(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        write_log("Арифметические операции (Сложение): ValueError", "Ошибка: Введено не числовое значение")
        return "\033[31m[ Ошибка: Введено недопустимое значение ]\033[0m"
    else:
        return round(a+b, 2)


def minus(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        write_log("Арифметические операции (Вычитание): ValueError", "Ошибка: Введено не числовое значение")
        return "\033[31m[ Ошибка: Введено недопустимое значение ]\033[0m"
    else:
        return round(a-b, 2)


def divide(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        write_log("Арифметические операции (Деление): ValueError", "Ошибка: Введено не числовое значение")
        return "\033[31m[ Ошибка: Введено недопустимое значение ]\033[0m"
    else:
        try: a/b or b/a
        except ZeroDivisionError:
            write_log("Арифметические операции (Деление): ZeroDivisionError", "")
            return "\u001b[33m[ Внимание: На ноль делить нельзя ]\u001b[0m"
        else:
            return round(a/b, 2)


def full_divide(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        write_log("Арифметические операции (Целочисленное деление): ValueError", "Ошибка: Введено не числовое значение")
        return "\033[31m[ Ошибка: Введено недопустимое значение ]\033[0m"
    else:
        try: a//b or b//a
        except ZeroDivisionError:
            write_log("Арифметические операции (Целочисленное деление): ZeroDivisionError", "Внимание: На ноль делить нельзя")
            return "\u001b[33m[ Внимание: На ноль делить нельзя ]\u001b[0m"
        else:
                return round(a//b, 2)


def multiply(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        write_log("Арифметические операции (Умножение): ValueError", "Ошибка: Введено не числовое значение")
        return "\033[31m[ Ошибка: Введено недопустимое значение ]\033[0m"
    else:
        return round(a*b, 2)


def remainder(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        write_log("Арифметические операции (Нахождение остатка): ValueError", "Ошибка: Введено не числовое значение")
        return "\033[31m[ Ошибка: Введено недопустимое значение ]\033[0m"
    else:
        try: a%b or b%a
        except ZeroDivisionError:
            write_log("Арифметические операции (Нахождение остатка): ZeroDivisionError", "Внимание: Остатка от нуля не существует")
            return "\u001b[33m[ Внимание: Остатка от нуля не существует ]\u001b[0m"
        else:
            return round(a%b, 2)

