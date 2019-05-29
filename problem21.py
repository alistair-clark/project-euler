'''
Project Euler
Problem #21: Amicable numbers

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

Date: May 28, 2019
'''

def sumDivisors(num):
    result = [1]
    for d in range (2, int(num ** 0.5 + 1)):
        if num % d == 0:
            result.extend([d, num//d])
    return sum(result)

sumDivisors(284)

def amicable_pair(number):
    result = []
    for x in range(1, number+1):
        y = sumDivisors(x)
        if sumDivisors(y) == x and x != y:
            result.append(tuple(sorted((x,y))))
    return set(result)

# this next step is not efficient...
sum(list(map(sum, amicable_pair(10000))))
