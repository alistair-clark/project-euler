'''
Project Euler
Problem #20: Factorial digit sum

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

Date: May 27, 2019
'''
def fact(num):
    """
    Returns the factorial of a num
    """
    tot = 1
    # base case
    if num == 1:
        return num
    else:
        tot = num * fact(num - 1)
    return tot

def Digits(num):
    tot = 0
    tot = sum([int(i) for i in str(num)])
    return tot

def factDigits(num):
    return Digits(fact(num))

factDigits(100)
