#!/usr/bin/python3
"""Prime Game
"""


def isWinner(x, nums):
    """Determines the winner of a prime game session with `x` rounds."""
    if x < 1 or not nums:
        return None

    marias_wins = 0
    bens_wins = 0

    # generate primes with a limit of the maximum number in nums
    n = max(nums)
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i**2, n + 1, i):
                primes[j] = False

    # count the number of primes less than n in nums for each round
    for n in nums:
        primes_count = sum(primes[2:n+1])
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1

    if marias_wins == bens_wins:
        return None

    return 'Maria' if marias_wins > bens_wins else 'Ben'
