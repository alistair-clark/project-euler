'''
Project Euler:
Problem #7: 10001st prime
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10,001st prime number?

Date: May 5, 2019
'''
# Here is the simple solution with the SymPy package
import sympy
sympy.prime(10001)


# Here is a more complicated (and slower) solution
def primes(n):
    primes = [2]
    attempt = 3
    while len(primes) < n:
        if all(attempt % prime != 0 for prime in primes):
            primes.append(attempt)
        attempt += 2
    return primes[-1]
primes(10001)
