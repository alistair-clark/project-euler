'''
Project Euler
Problem #13: Longest Collatz sequence

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.


Date: May 16, 2019
'''
import time

def collatzSeq(num):
    """Function returns the number of terms in a Collatz sequence for argument num."""

    n = num
    count = 1
    while n != 1:
        if n % 2 == 0:
            n /=2
        else:
            n = 3*n+1
        count += 1
    return count

def collatzMax(limit):
    """Returns the number with the longest Collatz sequence under the argument limit."""
    maxCollatz = 0
    maxNum = 0
    num = limit//2+1 # Largest num will be in top half of limit
    while num <= limit:
        tempCollatz = collatzSeq(num)
        if tempCollatz > maxCollatz:
            maxCollatz = tempCollatz
            maxNum = num
        num += 2 # Largest num will be odd
    return maxNum

start = time.time()
collatzMax(1000000)
print("time taken: %s seconds" %(time.time() - start))
