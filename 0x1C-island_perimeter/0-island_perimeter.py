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
    retorno = []
    for i, row in enumerate(grid):
        renglon = []
        for j, g in enumerate(row):
            numero = 0
            if g == 1:
                numero = 4
            # Arriba
                try:
                    if grid[i - 1][j] == 1:
                        numero -= 1
                except Exception as e:
                    pass
            # Abajo
                try:
                    if grid[i + 1][j] == 1:
                        numero -= 1
                except Exception as e:
                    pass
            # Izquierda
                try:
                    if grid[i][j - 1] == 1:
                        numero -= 1
                except Exception as e:
                    pass
            # Derecha
                try:
                    if grid[i][j + 1] == 1:
                        numero -= 1
                except Exception as e:
                    pass
            renglon.append(numero)
        retorno.append(renglon)
    return sum([sum(x) for x in retorno])
