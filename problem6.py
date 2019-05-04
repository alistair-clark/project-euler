'''
Project Euler:
Problem #6: Sum square difference
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers
and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.

Date: May 4, 2019
'''
def sumSquares(num):
    """
    Assumes num is an integer > 0.
    Function calculates the sum of the squares of the first "num" natural numbers.
    e.g. 1^2 + 2^2 + ... + 10^2 = 385
    """
    sum = 0
    for i in range(1,num+1):
        sum += i**2
    return sum

def sqaureSums(num):
    """
    Assumes num is an integer > 0.
    Function calculates the square of the sum of the first "num" natural numbers.
    (1 + 2 + ... + 10)^2 = 55^2 = 3025
    """
    sum = 0
    for i in range(1, num+1):
        sum += i
    return sum**2

def sumSqaureDifference(num):
    """
    Assumes num is an integer > 0.
    Function calculates the difference between the sum of the squares of the first
    "num" natural numbers and the square of the sum.
    """
    return sqaureSums(num) - sumSquares(num)

sumSqaureDifference(100)
