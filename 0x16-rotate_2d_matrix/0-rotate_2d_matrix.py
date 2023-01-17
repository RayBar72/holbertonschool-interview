#!/usr/bin/python3
"""
Module 0x16. Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    largo = len(matrix)
    largo

    copia = []
    for i in range(largo):
        r_copia = []
        for j in range(largo):
            r_copia.append(matrix[largo - 1 - j][i])
        copia.append(r_copia)
    copia

    for i in range(largo):
        matrix[i] = copia[i]
    matrix
