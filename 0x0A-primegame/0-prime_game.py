#!/usr/bin/python3

def isWinner(x, nums):
    """
    Determines the winner of the prime game.

    Args:
        x (int): Number of rounds.
        nums (list of int): List of n values for each round.

    Returns:
        str: Name of the player with the most wins ("Maria" or "Ben") or None if tied.
    """
    if not nums or x <= 0:
        return None

    # Determine the maximum value of n in nums
    max_num = max(nums)

    # Precompute prime numbers using the Sieve of Eratosthenes
    sieve = [True] * (max_num + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes
    for i in range(2, int(max_num**0.5) + 1):
        if sieve[i]:
            for multiple in range(i * i, max_num + 1, i):
                sieve[multiple] = False

    # Precompute the number of primes up to each number
    primes_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        primes_count[i] = primes_count[i - 1] + (1 if sieve[i] else 0)

    # Initialize scores for Maria and Ben
    maria_wins = 0
    ben_wins = 0

    # Play each round
    for n in nums:
        if primes_count[n] % 2 == 1:
            # Maria wins if the number of primes up to n is odd
            maria_wins += 1
        else:
            # Ben wins if the number of primes up to n is even
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Example usage
if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))

