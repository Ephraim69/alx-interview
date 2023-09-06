v#!/usr/bin/python3

def is_prime(n):
    """
    Check if a number is prime.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_next_prime(lst):
    """
    Return the next prime from the list.
    """
    for num in lst:
        if is_prime(num):
            return num
    return None


def is_winner(x, nums):
    """
    Determine the winner of the prime game over x rounds with nums as rounds.
    """
    winners = []

    for n in nums:
        numbers = set(range(2, n + 1))
        turn = "Maria"

        while True:
            prime = get_next_prime(numbers)
            if prime is None:
                winners.append("Ben" if turn == "Maria" else "Maria")
                break

            multiples = set(range(prime, n + 1, prime))
            numbers -= multiples

            turn = "Ben" if turn == "Maria" else "Maria"

    maria_wins = winners.count("Maria")
    ben_wins = winners.count("Ben")

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None


# For testing
if __name__ == "__main__":
    print("Winner: {}".format(is_winner(5, [2, 5, 1, 4, 3])))
