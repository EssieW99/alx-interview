#!/usr/bin/python3
""" a prime game"""


def isWinner(x, nums):
    """
    determines the winner of each game
    """
    def sieve(max_n):
        """
        generates a list of primes up to a maximum of max_n
        """

        is_prime = [True] * (max_n + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(max_n**0.5) + 1):
            if is_prime[i]:
                for multiple in range(i * i, max_n + 1, i):
                    is_prime[multiple] = False
        count = [0] * (max_n + 1)
        for i in range(1, max_n + 1):
            count[i] = count[i - 1] + (1 if is_prime[i] else 0)
        return is_prime, count

    max_n = max(nums)

    is_prime, count = sieve(max_n)

    marias_wins = 0
    bens_wins = 0

    for n in nums:
        num_primes = count[n]
        if num_primes % 2 == 1:
            marias_wins += 1
        else:
            bens_wins += 1

    if marias_wins > bens_wins:
        return 'Maria'
    elif bens_wins > marias_wins:
        return 'Ben'
    else:
        return None
