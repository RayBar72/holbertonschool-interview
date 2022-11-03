#!/usr/bin/python3
'''Modulus that solves N-queens problem'''
import sys


def busqueda(n, q, maldita):
    '''Function that searches in a given board'''
    never = []
    lista = [x for x in range(q, n * n)]
    matrix = []
    y = 0
    for i in range(n):
        renglon = []
        for j in range(n):
            renglon.append(y)
            y += 1
        matrix.append(renglon)
    renglon = q // n
    columna = q % n

    row = [x for x in lista if x < (n * (q // n + 1))]

    col = [x for x in lista if x in [x for x in range(q, n * n, n)]]

    d_menos = []
    for i in range(n):
        for j in range(n):
            if i - j == renglon - columna:
                d_menos.append(matrix[i][j])

    d_mas = []
    for i in range(n):
        for j in range(n):
            if i + j == renglon + columna:
                d_mas.append(matrix[i][j])

    maldita = row + col + d_menos + d_mas + maldita
    maldita = list(set(maldita))
    for i in maldita:
        never.append(i)

    posible = [x for x in lista if x not in maldita if x not in never]
    ahora = [x for x in posible if x in matrix[renglon + 1]]
    papa = [q]
    return [len(ahora)], ahora, papa, maldita


def listo(n, listar):
    '''
    Function that takes care different posibilities for
    queen initial position in the board
    '''
    retornar = []
    lento = []
    for i, l in enumerate(listar[0]):
        pos = i * 3 + 1
        for j, p in enumerate(listar[pos]):
            x = busqueda(n, p, listar[pos + 2])
            if x[0][0] != 0:
                lento = lento + x[0]
                retornar.append(x[1])
                retornar.append(listar[pos + 1] + x[2])
                retornar.append(x[3])
            else:
                pass
    retornar.insert(0, lento)
    return tuple(retornar)


def coordenadas(n, q):
    x = busqueda(n, q, [])
    queentionary = {}
    for i in range(n - 1):
        try:
            lento = x[0]
            lista = list(x)
            queentionary[i + 2] = lista
            x = listo(n, lista)
        except Exception as e:
            break
    if queentionary.get(n) is not None:
        queen = queentionary[n]
        reinitas = []
        for i, l in enumerate(queen[0]):
            pos = i * 3 + 1
            for j, p in enumerate(queen[pos]):
                reinitas.append(queen[pos + 1] + [p])
        coordenadas = []
        for row in reinitas:
            for r in row:
                cero = r // n
                uno = r % n
                coordenadas.append([cero, uno])
        return coordenadas
    else:
        return None


# def myqueens(n):
if __name__ == '__main__':
    '''Main function that calculates queens challange'''
    import sys

    # if len(sys.argv) != 2:
    #     print("Usage: nqueens N")
    #     sys.exit(1)

    n = sys.argv[1]

    if n.isdigit() is False:
        print("N must be a number")
        sys.exit(1)

    n = int(n)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    for i in range(n):
        x = coordenadas(n, i)
        if x is not None and x != []:
            print(x)
