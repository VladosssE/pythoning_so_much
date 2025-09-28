def matrix_create(a, b):
    Matrix = []
    if a == 0 or b == 0:
        print("\u001b[33m\n[ Значения длины либо ширины матрицы равны нулю ]\u001b[0m")
        Matrix = ["Создание матрицы произошло с ошибками (a и/или b = 0)"]
    elif a < 0 or b < 0:
        print("\033[31m\n[ Ошибка: отрицательная ширина либо длина матрицы ]\033[0m")
        Matrix = ["Создание матрицы произошло с ошибками (a и/или b < 0)"]
    else:
        for i in range(a):
            n = []
            for j in range(b):
                try:
                    m = input("Введите элементы матрицы: ")
                except ValueError:
                    print("\033[31m\n[ Введено недопустимое значение (???) ]\033[0m")
                n.append(m)
            Matrix.append(n)
    return Matrix
