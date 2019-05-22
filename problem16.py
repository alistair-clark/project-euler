'''
Project Euler
Problem #16: Power digit sum

2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?

Date: May 22, 2019
'''

def powerDigitSum(power):
    num = 2**power
    sum = 0
    for digit in str(num):
        sum += int(digit)
    return sum

print(powerDigitSum(1000))

#alternative method. map() creates an iterable of ints that is summed
sum(map(int, str(2**1000)))
