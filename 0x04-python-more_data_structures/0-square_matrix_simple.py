#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        new_matrix.append([x**2 for x in i])
    return new_matrix
