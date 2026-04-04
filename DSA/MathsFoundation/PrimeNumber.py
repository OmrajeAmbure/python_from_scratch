# Prime Number Algorithms and Sieve Techniques
"""
A prime number is a natural number greater than 1 that has exactly two distinct positive divisors — 1 and itself.

Basic Primality Check: To check if a number n is prime, try dividing it by numbers from 2 to n-1. If any number divides it, then n is not prime; otherwise, it is.

Optimized Method (Square Root Check): We only need to check up to √n because if n has a factor larger than √n, the corresponding smaller factor must be less than √n.

So if no number from 2 to √n divides n, then n is prime.
"""
import math


def isPrime(n):
    # Check if n is 1 or 0
    if n <= 1:
        return False

    # Check if n is 2 or 3
    if n == 2 or n == 3:
        return True

    # Check whether n is divisible by 2 or 3
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Check from 5 to square root of n
    # Iterate i by (i+6)
    i = 5
    while i <= math.sqrt(n):
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


if __name__ == "__main__":
    n = 25
    if (isPrime(n)):
        print("true")
    else:
        print("false")