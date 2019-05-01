'''
Project Euler
Problem #3: Largest prime factor
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''

def LargestPrimeFactor(num):
    """
    Input: num, a positive int
    Returns the largest prime factor of num
    """
    factors = []
    d = 2 # Setting at 2 since this is the first non-trivial factor
    while num > 1:
        while num % d == 0:
            factors.append(d)
            num /= d
        d += 1

    return max(factors)


LargestPrimeFactor(600851475143)
