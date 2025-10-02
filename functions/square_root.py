from math import sqrt
from .create_all_files import write_log
def square_root_formula(a, b, c):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        write_log("Квадратный корень (Формула): ValueError", "Ошибка: Введено не числовое значение")
        er_message = "Введено недопустимое значение"
        formula = "-"
    elif a==0 or b==0 or c==0:
        write_log("Квадратный корень (Формула): ZeroInputError", "Программа не может решать неполные квадратные уравнения")
        er_message = "Введено нулевое значение"
        formula = "-"
    else:
        er_message = "Успешно"
        formula = f"{a}x^2 + {b}x + {c} = 0"
    return er_message, formula

def discriminant(a, b, c):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        write_log("Квадратный корень (Дискриминант): ValueError", "Ошибка: Введено не числовое значени")
        er_message = "Введено недопустимое значение"
        D = "-"
    elif a==0 or b==0 or c==0:
        write_log("Квадратный корень (Дискриминант): ZeroInputError", "Программа не может решать неполные квадратные уравнения")
        er_message = "Введено нулевое значение"
        D = "-"
    else:
        er_message = "Успешно"
        D = b**2 - 4*a*c
    return er_message, D

def square_root_mathing(a, b, c, D):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        write_log("Квадратный корень (Решение): ValueError", "Ошибка: Введено не числовое значени")
        er_message = "Введено недопустимое значение"
        x1 = "-"
        x2 = "-"
    elif a==0 or b==0 or c==0:
        write_log("Квадратный корень (Решение): ZeroInputError", "Программа не может решать неполные квадратные уравнения")
        er_message = "Введено нулевое значение"
        x1 = "-"
        x2 = "-"
    elif D > 0:
        try:
            er_message = "Успешно"
            x1 = round((-b + sqrt(D)) / (2*a), 2)
            x2 = round((-b - sqrt(D)) / (2*a), 2)
        except ZeroDivisionError:
            x1 = "-"
            x2 = "-"
    elif D == 0:
        try:
            er_message = "Успешно"
            x1 = round((-b + sqrt(D)) / (2*a), 2)
            x2 = "-"
        except ZeroDivisionError:
            x1 = "-"
            x2 = "-"
        return x1
    elif D < 0:
        er_message = "Корней нет"
        x1 = "-"
        x2 = "-"
    else:
        pass
    return er_message, x1, x2
