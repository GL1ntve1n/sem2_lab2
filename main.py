import numpy as np
from numpy import linalg

size = int(input('Введите размерность матрицы от 1 до 31:'))
while (size < 1) or (size > 31):
    size = int(input("Вы ввели неверное число, введите размерность матрицы от 1 до 31:"))


matrix = np.random.randint(5, size=(size, size))
rank = np.linalg.matrix_rank(matrix)


print("Матрица:\n", matrix)
print("Ранг матрицы:", rank)
t = int(input('Введите количество знаков после запятой:'))


t = 0.1 ** t
n = 1
fact = 1
summ = 0
flag_summ = 0
diff = 1
while abs(diff) > t:
    flag_summ += summ
    summ += (-1**(n-1))*(np.linalg.det(linalg.matrix_power(matrix, 2 * n))) / fact
    n += 1
    fact = fact * (2*n) * (2*n - 1)
    diff = abs(flag_summ-summ)
    flag_summ = 0
    print(n-1, ':', summ, ' ', diff)
print('Сумма знакопеременного ряда:', summ)
