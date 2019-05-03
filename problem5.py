'''
Project Euler:
Problem #5: Smallest multiple
2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by
all of the numbers from 1 to 20?

Date: May 3, 2019
'''
from fractions import gcd
def lcm(a,b):
    "Calculate the lowest common multiple of two integers a and b"
    return a*b//gcd(a,b)

from functools import reduce
reduce(lcm, range(1,20+1))

# Lessons learned --> don't brute force solutions. Learn to use existing tools and libraries
