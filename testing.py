import textwrap
from functions import *
def testing_arithmetic_operations():
    try:
        op, er_message_sum_1, result_sum_1 = plus(1, 1)
        op, er_message_sum_2, result_sum_2 = plus(0, 1)
        op, er_message_sum_3, result_sum_3 = plus(0.4, 7)
        op, er_message_sum_4, result_sum_4 = plus("melon", 42)

        op, er_message_minus_1, result_minus_1 = minus(1, 1)
        op, er_message_minus_2, result_minus_2 = minus(0, 1)
        op, er_message_minus_3, result_minus_3 = minus(0.4, 7)
        op, er_message_minus_4, result_minus_4 = minus("melon", 42)
    
        op, er_message_divide_1, result_divide_1 = divide(1, 1)
        op, er_message_divide_2, result_divide_2 = divide(0, 1)
        op, er_message_divide_3, result_divide_3 = divide(0.4, 7)
        op, er_message_divide_4, result_divide_4 = divide("melon", 42)
    
        op, er_message_full_divide_1, result_full_divide_1 = full_divide(1, 1)
        op, er_message_full_divide_2, result_full_divide_2 = full_divide(0, 1)
        op, er_message_full_divide_3, result_full_divide_3 = full_divide(0.4, 7)
        op, er_message_full_divide_4, result_full_divide_4 = full_divide("melon", 42)

        op, er_message_multiply_1, result_multiply_1 = multiply(1, 1)
        op, er_message_multiply_2, result_multiply_2 = multiply(0, 1)
        op, er_message_multiply_3, result_multiply_3 = multiply(0.4, 7)
        op, er_message_multiply_4, result_multiply_4 = multiply("melon", 42)

        op, er_message_remainder_1, result_remainder_1 = remainder(1, 1)
        op, er_message_remainder_2, result_remainder_2 = remainder(0, 1)
        op, er_message_remainder_3, result_remainder_3 = remainder(0.4, 7)
        op, er_message_remainder_4, result_remainder_4 = remainder("melon", 42)

        print(textwrap.dedent(
        f"""
        [ \u001b[36m{'Арифметические операции':-^89}\u001b[0m ]
        [ {'Сложение':21} ][ {'a = 1, b = 1':18} ] = [ {result_sum_1:^5} ] [ {er_message_sum_1:29} ]
        [ {'Сложение':21} ][ {'a = 0, b = 1':18} ] = [ {result_sum_2:^5} ] [ {er_message_sum_2:29} ]
        [ {'Сложение':21} ][ {'a = 0.4, b = 7':18} ] = [ {result_sum_3:^5} ] [ {er_message_sum_3:29} ]
        [ {'Сложение':21} ][ {'a = melon, b = 42':18} ] = [ {result_sum_4:^5} ] [ {er_message_sum_4:29} ]

        [ {'Вычитание':21} ][ {'a = 1, b = 1':18} ] = [ {result_minus_1:^5} ] [ {er_message_minus_1:29} ]
        [ {'Вычитание':21} ][ {'a = 0, b = 1':18} ] = [ {result_minus_2:^5} ] [ {er_message_minus_2:29} ]
        [ {'Вычитание':21} ][ {'a = 0.4, b = 7':18} ] = [ {result_minus_3:^5} ] [ {er_message_minus_3:29} ]
        [ {'Вычитание':21} ][ {'a = melon, b = 42':18} ] = [ {result_minus_4:^5} ] [ {er_message_minus_4:29} ]
    
        [ {'Деление':21} ][ {'a = 1, b = 1':18} ] = [ {result_divide_1:^5} ] [ {er_message_divide_1:29} ]
        [ {'Деление':21} ][ {'a = 0, b = 1':18} ] = [ {result_divide_2:^5} ] [ {er_message_divide_2:29} ]
        [ {'Деление':21} ][ {'a = 0.4, b = 7':18} ] = [ {result_divide_3:^5} ] [ {er_message_divide_3:29} ]
        [ {'Деление':21} ][ {'a = melon, b = 42':18} ] = [ {result_divide_4:^5} ] [ {er_message_divide_4:29} ]
    
        [ {'Целочисленное деление':21} ][ {'a = 1, b = 1':18} ] = [ {result_full_divide_1:^5} ] [ {er_message_full_divide_1:29} ]
        [ {'Целочисленное деление':21} ][ {'a = 0, b = 1':18} ] = [ {result_full_divide_2:^5} ] [ {er_message_full_divide_2:29} ]
        [ {'Целочисленное деление':21} ][ {'a = 0.4, b = 7':18} ] = [ {result_full_divide_3:^5} ] [ {er_message_full_divide_3:29} ]
        [ {'Целочисленное деление':21} ][ {'a = melon, b = 42':18} ] = [ {result_full_divide_4:^5} ] [ {er_message_full_divide_4:29} ]
    
        [ {'Умножение':21} ][ {'a = 1, b = 1':18} ] = [ {result_multiply_1:^5} ] [ {er_message_multiply_1:29} ]
        [ {'Умножение':21} ][ {'a = 0, b = 1':18} ] = [ {result_multiply_2:^5} ] [ {er_message_multiply_2:29} ]
        [ {'Умножение':21} ][ {'a = 0.4, b = 7':18} ] = [ {result_multiply_3:^5} ] [ {er_message_multiply_3:29} ]
        [ {'Умножение':21} ][ {'a = melon, b = 42':18} ] = [ {result_multiply_4:^5} ] [ {er_message_multiply_4:29} ]
    
        [ {'Нахождение остатка':21} ][ {'a = 1, b = 1':18} ] = [ {result_remainder_1:^5} ] [ {er_message_remainder_1:29} ]
        [ {'Нахождение остатка':21} ][ {'a = 0, b = 1':18} ] = [ {result_remainder_2:^5} ] [ {er_message_remainder_2:29} ]
        [ {'Нахождение остатка':21} ][ {'a = 0.4, b = 7':18} ] = [ {result_remainder_3:^5} ] [ {er_message_remainder_3:29} ]
        [ {'Нахождение остатка':21} ][ {'a = melon, b = 42':18} ] = [ {result_remainder_4:^5} ] [ {er_message_remainder_4:29} ]
        """
        ).strip())
    except Exception as e:
        return print(f"\u001b[31mПроизошла ошибка {e}\u001b[0m")
    return 0


def testing_square_root():
    try:
        er_message_formula_1, formula_1 = square_root_formula(1, 1, 1)
        er_message_formula_2, formula_2 = square_root_formula(0, 0, 0)
        er_message_formula_3, formula_3 = square_root_formula(1.6, 1.1, 1.9)
        er_message_formula_4, formula_4 = square_root_formula("melon", 1, 0)

        er_message_D_1, D_1 = discriminant(1, 1, 1)
        er_message_D_2, D_2 = discriminant(0, 0, 0)
        er_message_D_3, D_3 = discriminant(1.6, 1.1, 1.9)
        er_message_D_4, D_4 = discriminant("melon", 1, 0)

        er_message_mathing_1, ax_1, bx_1 = square_root_mathing(1, 1, 1, 1)
        er_message_mathing_2, ax_2, bx_2 = square_root_mathing(1, 1, 1, 0)
        er_message_mathing_3, ax_3, bx_3 = square_root_mathing(1, 1, 1, -1)
        er_message_mathing_4, ax_4, bx_4 = square_root_mathing(0, 0, 0, 0)
        er_message_mathing_5, ax_5, bx_5 = square_root_mathing("ff", 1, 0, 1)

        print(textwrap.dedent(
        f"""
        [ \u001b[36m{'Квадратное уравнение':-^108}\u001b[0m ]
        [ {'Формула':12} ][ {'a = 1, b = 1, c = 1':27} ] = [ {formula_1:^23} ] [ {er_message_formula_1:30} ]
        [ {'Формула':12} ][ {'a = 0, b = 0, c = 0':27} ] = [ {formula_2:^23} ] [ {er_message_formula_2:30} ]
        [ {'Формула':12} ][ {'a = 1.6, b = 1.1, c = 1.9':27} ] = [ {formula_3:^23} ] [ {er_message_formula_3:30} ]
        [ {'Формула':12} ][ {'a = melon, b = 1, c = 0':27} ] = [ {formula_4:^23} ] [ {er_message_formula_4:30} ]

        [ {'Дискриминант':12} ][ {'a = 1, b = 1, c = 1':27} ] = [ {D_1:^23} ] [ {er_message_D_1:30} ]
        [ {'Дискриминант':12} ][ {'a = 0, b = 0, c = 0':27} ] = [ {D_2:^23} ] [ {er_message_D_2:30} ]
        [ {'Дискриминант':12} ][ {'a = 1.6, b = 1.1, c = 1.9':27} ] = [ {D_3:^23} ] [ {er_message_D_3:30} ]
        [ {'Дискриминант':12} ][ {'a = melon, b = 1, c = 0':27} ] = [ {D_4:^23} ] [ {er_message_D_4:30} ]

        [ {'Решение':12} ][ {'a = 1, b = 1, c = 1, D = 1':27} ] = [ {ax_1:^9} ] [ {bx_1:^9} ] [ {er_message_mathing_1:30} ]
        [ {'Решение':12} ][ {'a = 1, b = 1, c = 1, D = 0':27} ] = [ {ax_2:^9} ] [ {bx_2:^9} ] [ {er_message_mathing_2:30} ]
        [ {'Решение':12} ][ {'a = 1, b = 1, c = 1, D = -1':27} ] = [ {ax_3:^9} ] [ {bx_3:^9} ] [ {er_message_mathing_3:30} ]
        [ {'Решение':12} ][ {'a = 0, b = 0, c = 0, D = 0':27} ] = [ {ax_4:^9} ] [ {bx_4:^9} ] [ {er_message_mathing_4:30} ]
        [ {'Решение':12} ][ {'a = ff, b = 1, c = 0, D = 1':27} ] = [ {ax_5:^9} ] [ {bx_5:^9} ] [ {er_message_mathing_5:30} ]
        """
        ).strip())
    except Exception as e:
        return print(f"\u001b[31mПроизошла ошибка {e}\u001b[0m")
    return 0


def testing_factorial():
    try:
        er_message_1, factorial_1 = fact(5)
        er_message_2, factorial_2 = fact(0)
        er_message_3, factorial_3 = fact(-5)
        er_message_4, factorial_4 = fact("t")

        print(textwrap.dedent(
        f"""
        [ \u001b[36m{'Факториал':-^66}\u001b[0m ]
        [ Факториал ][ {'num = 5':8} ] = [ {factorial_1:^3} ] [ {er_message_1:30} ]
        [ Факториал ][ {'num = 0':8} ] = [ {factorial_2:^3} ] [ {er_message_2:30} ]
        [ Факториал ][ {'num = -5':8} ] = [ {factorial_3:^3} ] [ {er_message_3:30} ]
        [ Факториал ][ {'num = t':8} ] = [ {factorial_4:^3} ] [ {er_message_4:30} ]
        """
        ).strip())
    except Exception as e:
        return print(f"\u001b[31mПроизошла ошибка {e}\u001b[0m")
    return 0


def testing_caesar_ascii():
    try:
        er_message_1, result_1 = caesar_ascii("apple", 3)
        er_message_2, result_2 = caesar_ascii("apple", 0)
        er_message_3, result_3 = caesar_ascii("apple", -3)
        er_message_4, result_4 = caesar_ascii("apple", -800)
        er_message_5, result_5 = caesar_ascii("apple", 1200)
        er_message_6, result_6 = caesar_ascii("apple", "melon")

        print(textwrap.dedent(
        f"""
        [ \u001b[36m{'Шифр Цезаря (ASCII)':-^115}\u001b[0m ]
        [ Шифр Цезаря ][ {'Строка = apple, Смещение = 3':32} ] = [ {result_1:^5} ] [ {er_message_1:51} ]
        [ Шифр Цезаря ][ {'Строка = apple, Смещение = 0':32} ] = [ {result_2:^5} ] [ {er_message_2:51} ]
        [ Шифр Цезаря ][ {'Строка = apple, Смещение = -3':32} ] = [ {result_3:^5} ] [ {er_message_3:51} ]
        [ Шифр Цезаря ][ {'Строка = apple, Смещение = -800':32} ] = [ {result_4:^5} ] [ {er_message_4:51} ]
        [ Шифр Цезаря ][ {'Строка = apple, Смещение = 1200':32} ] = [ {result_5:^5} ] [ {er_message_5:51} ]
        [ Шифр Цезаря ][ {'Строка = apple, Смещение = melon':32} ] = [ {result_6:^5} ] [ {er_message_6:51} ]
        """
        ).strip())
    except Exception as e:
        return print(f"\u001b[31mПроизошла ошибка {e}\u001b[0m")
    return 0


def testing_caesar_dictionary():
    try:
        er_message_1, result_1 = caesar_dictionary("apple", 3)
        er_message_2, result_2 = caesar_dictionary("apple", 0)
        er_message_3, result_3 = caesar_dictionary("apple", -3)
        er_message_4, result_4 = caesar_dictionary("apple", -800)
        er_message_5, result_5 = caesar_dictionary("apple", 1200)
        er_message_6, result_6 = caesar_dictionary("apple", "melon")

        print(textwrap.dedent(
        f"""
        [ \u001b[36m{'Шифр Цезаря (Словарь)':-^115}\u001b[0m ]
        [ Шифр Цезаря ][ {'Строка = apple, Смещение = 3':32} ] = [ {result_1:^5} ] [ {er_message_1:51} ]
        [ Шифр Цезаря ][ {'Строка = apple, Смещение = 0':32} ] = [ {result_2:^5} ] [ {er_message_2:51} ]
        [ Шифр Цезаря ][ {'Строка = apple, Смещение = -3':32} ] = [ {result_3:^5} ] [ {er_message_3:51} ]
        [ Шифр Цезаря ][ {'Строка = apple, Смещение = -800':32} ] = [ {result_4:^5} ] [ {er_message_4:51} ]
        [ Шифр Цезаря ][ {'Строка = apple, Смещение = 1200':32} ] = [ {result_5:^5} ] [ {er_message_5:51} ]
        [ Шифр Цезаря ][ {'Строка = apple, Смещение = melon':32} ] = [ {result_6:^5} ] [ {er_message_6:51} ]
        """
        ).strip())
    except Exception as e:
        return print(f"\u001b[31mПроизошла ошибка {e}\u001b[0m")
    return 0


testing_arithmetic_operations()
testing_square_root()
testing_factorial()
testing_caesar_ascii()
testing_caesar_dictionary()
