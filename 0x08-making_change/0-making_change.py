#!/usr/bin/python3
""" a make change algorithm"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values, determine the fewest number
    of coins needed to meet a given amount total
    """

    if total <= 0:
        return 0

    new_list = [float('inf')] * (total + 1)
    new_list[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if i - coin >= 0:
                new_list[i] = min(new_list[i], new_list[i - coin] + 1)

    if new_list[total] != float('inf'):
        return new_list[total]
    else:
        return -1
