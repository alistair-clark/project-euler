'''
Project Euler:
Problem #23: Non-abundant sums

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

Date: May 30, 2019
'''
def sumDivisors(num):
    result = set()
    result.add(1)
    for d in range (2, int(num ** 0.5 + 1)):
        if num % d == 0:
            result.add(d)
            result.add(num//d)
    return sum(result)

def abundantNums(limit):
    result = []
    for i in range(1,limit):
        if i < sumDivisors(i):
            result.append(i)
    return result

def sumInList(numList, num):
    """Return True if 2 numbers from `numList` add up to num, False otherwise."""
    numSet = set(numList)
    return any(num-i in numSet for i in numSet)


result = 0
for i in range(1, 28124):
    if sumInList(abundantNumList, i) == False:
        result += i
print(result)
