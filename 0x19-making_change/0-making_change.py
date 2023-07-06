#!/usr/bin/python3
"""
0-making_chage.py
Modulus that works making chang
"""


def makeChange_sub(coins, total, solutions):
    """Function that calculates in recursive way
        a dynamic solution for making change problem
    Args:
        coins (list): coins available
        total (int): amount to use
        solutions (list): posible solutions
    Returns:
        int: -1 if no solution, 0 if total equal or less
        than 0 or fewest number of coins
    """
    if total < 0:
        return -1
    if total == 0:
        return 0

    if solutions[total - 1] != 0:
        return solutions[total - 1]

    optimal_solution = float('inf')

    for coin in coins:
        best_solution_for_coin = makeChange_sub(coins, total - coin, solutions)
        if 0 <= best_solution_for_coin < optimal_solution:
            optimal_solution = best_solution_for_coin + 1

    if optimal_solution == float('inf'):
        solutions[total - 1] = -1
    else:
        solutions[total - 1] = optimal_solution

    return solutions[total - 1]


def makeChange(coins, total):
    """Function that calculates making change problem
    Args:
        coins (list): coins available
        total (int): amount to use
    Returns:
        int: -1 if no solution, 0 if total equal or less
        than 0 or fewest number of coins
    """
    if total < 1:
        return 0
    else:
        return makeChange_sub(coins, total, [0] * total)