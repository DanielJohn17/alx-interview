#!/usr/bin/python3
"""
Module for making chamge.
"""


def makeChange(coins, total):
    """
    Determins the fewest number of coins needed
    to achuive total.
    """
    if total <= 0:
        return 0

    sum = 0
    coin_idx = 0
    coin_count = 0
    sorted_coins = sorted(coins, reverse=True)
    length = len(coins)

    while sum < total:
        if coin_idx >= length:
            return -1

        if sum + sorted_coins[coin_idx] <= total:
            sum += sorted_coins[coin_idx]
            coin_count += 1
        else:
            coin_idx += 1

    return coin_count
