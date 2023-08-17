#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    size = len(matrix)
    new_matrix = []
    for i in range(size):
        new_matrix.append(list(map(lambda x: x ** 2, matrix[i])))
    return new_matrix
