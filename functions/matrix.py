from .create_all_files import write_log
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
                    m = int(input("[ Введите элементы матрицы (Только числа) ] = "))
                except ValueError:
                    print("\033[31m[ Ошибка: введено не числовое значение ]\033[0m")
                    write_log("Сумма матриц: ValueError", "Ошибка: Введено не числовое значение")
                    m = 1
                n.append(m)
            Matrix.append(n)
    return Matrix


def matrix_sum(Matrix, Matrix2):
    summed_matrix = []
    if len(Matrix) != len(Matrix) or len(Matrix[0]) != len(Matrix2[0]):
        print("\033[31m[ Ошибка: Размеры двух матриц не совпадают ]\033[0m")
        write_log("Сумма матриц: Несовпадение размеров (Ошибка)", "Ошибка: Размеры двух матриц не совпадают")
        summed_matrix = ["ERROR"]
    else:
        for i in range(len(Matrix)):
            row = []
            for j in range(len(Matrix[0])):
                row.append(int(Matrix[i][j])+ int(Matrix2[i][j]))
            summed_matrix.append(row)
    return summed_matrix
