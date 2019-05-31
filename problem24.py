'''
Project Euler:
Problem #24: Lexicographic permutations

A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

Date: May 31, 2019
'''

from itertools import permutations
import math

# create a list of strings for numbers 0 through 9
strList = []
for i in range(10):
    strList.append(str(i))

# use permuations() to create an iterator of all permutations
perm = permutations(strList)
print(perm)

# create a list with all permuations
result = []
for i in perm:
    result.append(i)

# find the 1,000,000 number and turn it into an int
strNum= ''
for i in result[999999]:
    strNum += i
print(int(strNum))
