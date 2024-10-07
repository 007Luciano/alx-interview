#!/usr/bin/python3
"""makeChange module"""


def makeChange(coins: int, total: int) -> int:
    """
    An algorithm calculating change given a pile of coins.
    Args:
        coins: list of integers
        total: integer
    Returns:
        integer: minimum number of coins needed to make the total
    """
    if total <= 0:
        return 0

    dp = {0: 0}

    coins.sort(reverse=True)

    for coin in coins:
        for x in range(coin, total + 1):
            if x - coin in dp:
                if x not in dp:
                    dp[x] = dp[x - coin] + 1
                else:
                    dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[total] if total in dp else -1
