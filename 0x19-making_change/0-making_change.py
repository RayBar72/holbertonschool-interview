#!/usr/bin/python3
"""
0-making_chage.py
"""


def makeChange(coins, total):
    """Function that calculates making change problem
        Args:
            coins (list): coins available
            total (int): amount to use
        Returns:
            int: -1 if no solution, 0 if total equal or less
            than 0 or fewest number of coins
    """
    if total <= 0:
        return 0

    coins = sorted(coins, reverse=True)

    cuenta = 0

    for coin in coins:
        while total >= coin:
            total = total - coin
            cuenta = cuenta + 1

    if total != 0:
        return -1

    return cuenta
