#!/usr/bin/python3
""" pascal triangle """


def pascal_triangle(n):
    """ pascal triangle function """
    if n <= 0:
        return []

    result = [[1]]
    for i in range(1, n):
        row = [1]

        for j in range(1, i):
            element = result[i - 1][j - 1] + result[i - 1][j]
            row.append(element)
        row.append(1)
        result.append(row)

    return result
