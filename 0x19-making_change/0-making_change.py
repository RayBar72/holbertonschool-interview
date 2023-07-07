#!/usr/bin/python3
'''
0-making_chage.py
Modulus that works making chang
'''


def makeChange(coins, total):
    '''Function that calculates in recursive way
        a dynamic solution for making change problem
    Args:
        coins (list): coins available
        total (int): amount to use
    Returns:
        int: -1 if no solution, 0 if total equal or less
        than 0 or fewest number of coins
    '''
    if total <= 0:
        return 0

    coins = sorted(coins, reverse=True)

    count = 0

    for coin in coins:
        while total >= coin:
            total -= coin
            count += 1

    if total != 0:
        return -1
    else:
        return count
