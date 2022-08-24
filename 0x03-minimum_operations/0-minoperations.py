#!/usr/bin/python3
'''
Modulus that contains a method that calculates the
fewest number of operations needed to result in exactly
n H characters in the file.
'''


def minOperations(n):
    '''
    Method that calculates the fewest number of operations
    needed to result in exactly n H characters in the file.
    '''
    cp = 0
    pst = 1
    i = 2
    if not isinstance(n, int):
        return 0
    if n < 1:
        return 0
    ls = []
    while n > 1:
        i += 1
        if n % i == 0:
            while n % i == 0:
                n /= i
                ls.append(i)
    retono = sum(ls)
    return retono
