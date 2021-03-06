'''
Project Euler
Problem #12: Highly divisible triangular number
The sequence of triangle numbers is generated by adding the natural numbers.
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
The first ten terms would be: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?

Date: May 14, 2019
'''

import math
def numFactors(num):
    numFactors = 0
    for i in range(1, int(math.ceil(math.sqrt(num)))):
        if num % i == 0:
            numFactors += 2
        else:
            continue
    return numFactors

numDivisors = 0
triangleNumber = 1
counter = 1
while numDivisors < 500:
    numDivisors = numFactors(triangleNumber)
    if numDivisors >= 500:
        print(str(counter) + ", " + str(triangleNumber) + ", " + str(numDivisors))
        break
    else:
        counter += 1
        triangleNumber += counter
