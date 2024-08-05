def get_matrix(n, m, value):
    for i in range(int(n)):
        matrix.append([])
        for j in range(int(m)):
            matrix[i].append(value)
    print(matrix)

matrix = []
n = input('Введите количество строк: ')
m = input('Введите количество столбцов: ')
value = input('Введите значение: ')
get_matrix(n, m, value)

