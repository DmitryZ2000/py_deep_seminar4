# Напишите функцию для транспонирования матрицы


def print_matrix(my_list: list[int|float]) -> None:
    """ Printing out two-dimensional matrix """
    for item in my_list:
        print(*item)


# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print_matrix(matrix)

trans_matrix = list(zip(*matrix))

print('\nТранспорированный результат: \n')

print_matrix(matrix)
