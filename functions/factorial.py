def fact(a):
    fact = 1
    if not isinstance(a, (int)):
        return "\033[31m[ Ошибка: Введено недопустимое значение ]\033[0m"
    elif a < 0:
        return "\u001b[33m[ Для отрицательных чисел нет факториала ]\u001b[0m"
    elif a == 0:
        return "\u001b[33m[ Факториал 0 равен 1 ]\u001b[0m"
    else:
        for i in range(1, a+1):
            fact = fact * i
    return fact
