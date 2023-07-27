#!/usr/bin/python3
"""
0-island_perimeter
"""


def island_perimeter(grid):
    """Function that calculates the perimeter of an island

    Args:
        grid (list of list): Representation of the island

    Returns:
        int: perimeter
    """
    if type(grid) is not list and type(grid[0]) is not list:
        return 0
    retorno = []
    for i, row in enumerate(grid):
        for j, g in enumerate(row):
            numero = 0
            if g == 1:
                numero = 4
            # Arriba
                if i != 0:
                    if grid[i - 1][j] == 1:
                        numero -= 1
            # Abajo
                if i != len(grid) - 1:
                    if grid[i + 1][j] == 1:
                        numero -= 1
            # Izquierda
                if j != 0:
                    if grid[i][j - 1] == 1:
                        numero -= 1
            # Derecha
                if j != len(grid[0]) - 1:
                    if grid[i][j + 1] == 1:
                            numero -= 1
                retorno.append(numero)
    # return sum(retorno)
    return retorno
