def plus(a, b):
    return round(a+b, 2)


def minus(a, b):
    return round(a-b, 2)


def divide(a, b):
    try: a/b or b/a
    except ZeroDivisionError:
        return "Внимание: На ноль делить нельзя"
    else:
        return round(a/b, 2)


def full_divide(a, b):
    try: a//b or b//a
    except ZeroDivisionError:
        return "Внимание: На ноль делить нельзя"
    else:
        return round(a//b, 2)


def multiply(a, b):
    return round(a*b, 2)


def remainder(a, b):
    try: a%b or b%a
    except ZeroDivisionError:
        return "Внимание: Остатка от нуля не существует"
    else:
        return round(a%b, 2)
