from math import sqrt
def square_root_formula(a, b, c):
    if a==0 or b==0 or c==0:
        print("[ Программа не может решать неполные квадратные уравнения ]")
        formula = f"{a}x^2 + {b}x + {c} = 0"
    else:
        formula = f"{a}x^2 + {b}x + {c} = 0"
    return formula

def discriminant(a, b, c):
    if a==0 or b==0 or c==0:
        D = 0
    else:
        D = b**2 - 4*a*c
    return D

def square_root_mathing(a, b, c, D):
    if D > 0:
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
