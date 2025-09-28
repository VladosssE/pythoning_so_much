def fact(a):
    fact = 1
    if a < 0:
        print("\u001b[33m\n[ Для отрицательных чисел нет факториала ]\u001b[0m")
        fact = "Не определен"
    elif a == 0:
        print("\u001b[33m\n[ Факториал 0 равен 1 ]\u001b[0m")
        fact = 1
    else:
        for i in range(1, a+1):
            fact = fact * i
    return fact
