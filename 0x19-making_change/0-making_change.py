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
    dp = [float('inf')] * (total + 1)

    if total <= 0:
        return 0

    dp[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[total] == float('inf'):
        return -1

    return dp[total]
