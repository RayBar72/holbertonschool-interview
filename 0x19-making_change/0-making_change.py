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

    coins.sort(reverse=True)

    count = 0

    for coin in coins:
        while total >= coin:
            total -= coin
            count += 1

    if total != 0:
        return -1

    return count
