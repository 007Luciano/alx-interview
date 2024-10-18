#!/usr/bin/python3
"""
prime game module
"""


def isWinner(x, nums) -> str:
    """
    prime game function
    """
    if not nums or x <= 0:
        return None

    max_n = max(nums)

    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers

    for start in range(2, int(max_n**0.5) + 1):
        if sieve[start]:
            for multiple in range(start * start, max_n + 1, start):
                sieve[multiple] = False

    prime_counts = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_counts[i] = prime_counts[i - 1] + (1 if sieve[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_counts[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
