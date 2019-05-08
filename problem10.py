'''
Project Euler:
Problem #10: Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

Date: May 8, 2019
'''
# Solved using SymPy package
def sumPrimes(num):
    import sympy
    sumPrimes = sum(sympy.primerange(0,num))
    return sumPrimes

import time
start = time.time()
sumPrimes(2000000)
end = time.time()
print(end - start)

# solved using my own algorithm -- takes FOREVER
import time
start = time.time()
primes = [2]
nextPrime = 3
while nextPrime < 2000000:
    if all(nextPrime % prime != 0 for prime in primes):
        primes.append(nextPrime)
    nextPrime += 2
sum(primes)
end = time.time()
print(end - start)

# third algorithm. Faster because we only check up to the square root of the number
def isPrime(n):
    import math
    if n < 2: return "Neither prime, nor composite"
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

sum = 0
for i in range(2, 2000000):
    if isPrime(i):
        sum += i

print (sum)
