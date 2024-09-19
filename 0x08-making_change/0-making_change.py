#!/usr/bin/python3


"""Contains makeChange function"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total.
    
    Args:
    coins (list): A list of coin denominations.
    total (int): The target total.
    
    Returns:
    int: Fewest number of coins needed to meet total.
         If total is 0 or less, return 0.
         If total cannot be met by any number of coins you have, return -1.
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
