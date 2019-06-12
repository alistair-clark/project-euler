'''
Project Euler:
Problem #32: Pandigital products

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

Date: June 11, 2019
'''

def factors(num):
    """Returns a dictionary containing the multiplicand/multiplier factor pairings (not including 1) for the num"""
    factors = {}
    import math
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            factors[i] = num//i
    return factors

def pandigital(num, factors):
    """
    Checks to see if a number and any of it's multiplicand/multiplier factor pairings
    can be written as a 1 through 9 pandigital.

    For example, the multiplicand, multiplier, and product of 39 × 186 = 7254, is a 1 through 9 pandigital.

    Keyword arguments:
    num -- is a positive integer
    factors -- a dictionary containing the numbers multiplicand/multiplier factor pairings
    """
    pandigital = [1,2,3,4,5,6,7,8,9]
    for key, value in factors.items():
        strNum = str(num) + str(key) + str(value)
        intNum = [int(x) for x in strNum]
        intNum.sort()
        if intNum == pandigital:
            return True
    return False

# I wasn't sure what the upper and lower bounds should be, so I tried 10,000 and then 100,000, and found I got the same result
result = []
for num in range(10000):
    if pandigital(num, factors(num)) == True:
        result.append(num)
print(result)
sum(result)
