#!/usr/bin/env python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """Function def pascal_triangle(n): that returns a list
    of lists of integers representing the Pascal’s triangle of n

    Args:
        n (int): length of pascal triagle

    Returns:
        list or list of list: 0 if n <= 0 or the triangle
    """
    if n <= 0:
        return []

    retorno = []
    reng = 0
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0:
                row.append(1)
            elif j == reng:
                row.append(1)
            else:
                row.append(retorno[i - 1][j] + retorno[i - 1][j - 1])
        reng += 1
        retorno.append(row)

    return retorno
