'''
Project Euler:
Problem #26: Reciprocal cycles

A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

Date: May 31, 2019
'''
1/3

def cycleLength(num):
    """
    Function returns the length of the repeating decimals for 1/num
    """
    if 10 % num == 0: # if 10 mod num = 0, there's no repeating decimal
        return len(str(10//num))
    else:
        rems = set()
        rem = 10
        while True: # loop similates long division up until the remainder repeates itself
            rem = rem % num
            if rem in rems:
                return len(rems)
            else:
                rems.add(rem)
                rem *=10
cycleLength(10)

results = {}
for num in range(1,1000):
    results[num] = cycleLength(num)
max(zip(results.values(), results.keys()))
