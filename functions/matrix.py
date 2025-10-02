from .create_all_files import write_log
def matrix_create(a, b):
    Matrix = []
    if not isinstance(a, (int)) or not isinstance(b, (int)):
        write_log("Матрица: ValueError", "Введено недопустимое значение")
        er_message = "Создание матрицы произошло с ошибками (ValueError)"
        Matrix = "-"
    elif a == 0 or b == 0:
        write_log("Матрица: ZeroInputError", "Значения длины либо ширины матрицы равны нулю")
        er_message = "Создание матрицы произошло с ошибками (a и/или b = 0)"
        Matrix = "-"
    elif a < 0 or b < 0:
        write_log("Матрица: NegativeInputError", "Ошибка: отрицательная ширина либо длина матрицы")
        er_message = "Создание матрицы произошло с ошибками (a и/или b < 0)"
        Matrix = "-"
    else:
        for i in range(a):
            n = []
            for j in range(b):
                try:
                    m = int(input("[ Введите элементы матрицы (Только числа) ] = "))
                except ValueError:
                    write_log("Матрица: ValueError", "Ошибка: Введено не числовое значение")
                    er_message = "Ошибка: введено не числовое значение"
                    m = 1
                n.append(m)
            Matrix.append(n)
        er_message = "Успешно"
    return er_message, Matrix


def matrix_sum(Matrix, Matrix2):
    summed_matrix = []
    if isinstance(Matrix, (str)) or isinstance(Matrix2, (str)):
        write_log("Матрица: ValueError", "Введено недопустимое значение")
        er_message = "Создание матрицы произошло с ошибками (ValueError)"
        summed_matrix = "-"
    elif len(Matrix) != len(Matrix) or len(Matrix[0]) != len(Matrix2[0]):
        write_log("Сумма матриц: Несовпадение размеров (Ошибка)", "Ошибка: Размеры двух матриц не совпадают")
        er_message = "Ошибка: Размеры двух матриц не совпадают"
        summed_matrix = "-"
    else:
        for i in range(len(Matrix)):
            row = []
            for j in range(len(Matrix[0])):
                row.append(int(Matrix[i][j])+ int(Matrix2[i][j]))
            summed_matrix.append(row)
        er_message = "Успешно"
    return er_message, summed_matrix
