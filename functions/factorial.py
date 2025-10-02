from .create_all_files import write_log
def fact(num):
    factorial = 1
    if not isinstance(num, (int)):
        write_log("Факториал: ValueError", "Ошибка: Введено недопустимое значение")
        er_message = "Введено недопустимое значение"
        factorial = "-"
    elif num < 0:
        write_log("Факториал: NegativeInputError", "Для отрицательных чисел нет факториала")
        er_message = "Введено отрицательное значение"
        factorial = "-"
    elif num == 0:
        write_log("Факториал: ZeroInputError", "Факториал 0 равен 1")
        er_message = "Введено нулевое значение"
        factorial = 1
    else:
        er_message = "Успешно"
        for i in range(1, num+1):
            factorial = factorial * i
    return er_message, factorial
