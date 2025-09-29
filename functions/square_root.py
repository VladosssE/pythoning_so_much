from math import sqrt
def square_root_formula(a, b, c):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        return "\033[31m[ Ошибка: Введено недопустимое значение ]\033[0m"
    elif a==0 or b==0 or c==0:
        return "\u001b[33m[ Программа не может решать неполные квадратные уравнения ]\u001b[0m"
    else:
        formula = f"{a}x^2 + {b}x + {c} = 0"
    return formula

def discriminant(a, b, c):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        D = -1
        return "\033[31m[ Ошибка: Введено недопустимое значение ]\033[0m"
    elif a==0 or b==0 or c==0:
        D = -1
        return "\u001b[33m[ Программа не может решать неполные квадратные уравнения ]\u001b[0m"
    else:
        D = b**2 - 4*a*c
    return D

def square_root_mathing(a, b, c, D):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        return "\033[31m[ Ошибка: Введено недопустимое значение ]\033[0m"
    elif a==0 or b==0 or c==0:
        return "\u001b[33m[ Программа не может решать неполные квадратные уравнения ]\u001b[0m"
    elif D > 0:
        try:
            x1 = round((-b + sqrt(D)) / (2*a), 2)
            x2 = round((-b - sqrt(D)) / (2*a), 2)
        except ZeroDivisionError:
            x1 = 1
            x2 = 1
        return x1, x2
    elif D == 0:
        try:
            x1 = round((-b + sqrt(D)) / (2*a), 2)
        except ZeroDivisionError:
            x1 = 1
        return x1
    elif D < 0:
        return "Корней нет"
