def main_input():
    try:
        a = float(input("Введите значение a: "))
        b = float(input("Введите значение b: "))
    except ValueError:
        print("\u001b[31m\n[","Ошибка: Введено не числовое значение".center(50),"]\u001b[0m")
        write_log("Арифметические операции: ValueError", "Ошибка: Введено не числовое значение")
        finish = input("Любой ввод вернет в главное меню > ") # Пауза
    return clear_console(), starting_point()
