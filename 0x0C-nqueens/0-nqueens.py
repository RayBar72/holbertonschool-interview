#!/usr/bin/python3
'''Modulus that solves N-queens problem'''
import sys

def busqueda(n, q):
    '''Function that calculates the posible function'''
    lista = [x for x in range(q, n * n)]
    print(lista)

    row = [x for x in lista if x < n]
    print(row)

    col = [x for x in lista if x in [x for x in range(q, n * n, n)]]
    print(col)

    d_mas = [x for x in range(q, (n + 1) * q, n - 1)]
    print(d_mas)

    d_menos = [x for x in range(q, (n * n) - ( n * q), n + 1)]
    print(d_menos)

    maldita = row + col + d_menos + d_mas
    print(maldita)
    maldita = list(set(maldita))
    print(maldita)

    posible = [x for x in lista if x not in maldita]
    print(posible)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        exit(1)

    try:
        x = int(sys.argv[1])
    except Exception as e:
        print('N must be a number')
        exit(1)

    if x < 4:
        print('N must be at least 4')
        exit(1)

    for i in range(x):
        busqueda(x, i, 0)
    print(res)
