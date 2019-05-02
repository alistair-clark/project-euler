'''
Project Euler:
Problem #4: Largest palindrome product
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers
is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

Date: May 2, 2019
'''

# Here is my original, LESS efficient implementation

def isPal1(num):
    """
    Assumes input is an int. Returns True if num is a palindrome. False if not.
    """
    num = str(num)
    if len(num) == 1:
        return True
    elif len(num) == 2 and num[0] == num[1]:
        return True
    elif num[0] != num[-1]:
        return False
    else:
        num = num[1:-1]
        return isPal(num)

def largestNum(numDigits):
    """
    Finds the largest sum of two numbers with N-digits.
    For example, for 2-digits the largest sum is 99 * 99 = 9801
    """
    return int(str(9) * numDigits)

def smallestNum(numDigits):
    """
    Finds the smallest sum of two numbers with N-digits.
    For example, for 2-digits the smallest sum is 10 * 10 = 100
    """
    return int(str(1) + str(0) * (numDigits - 1))

def isSum(num, numDigits):
    """
    Checks if num is a possible sum of two n-digit numbers.
    """
    numList = [i for i in range(smallestNum(numDigits), largestNum(numDigits)+1)]
    sumList = set()
    for num1 in numList:
        for num2 in numList:
            sum = num1 * num2
            sumList.add(sum)
    if num in sumList:
        return True
    else:
        return False

def LargestPalProduct1(numDigits):
    """
    Finds the largest palindrome made from the product of two 2-digit numbers.
    For example, the largest palindrome from two 2-digit numbers
    is 9009 = 91 × 99.
    """
    num = largestNum(numDigits)**2
    while num >= smallestNum(numDigits)**2:
        if isPal2(num) == True and isSum(num, numDigits) == True:
            return num
        else:
            num -= 1
    print("There is no palindrome made from the product of two " + str(numDigits) + "-digit numbers.")


# Here is my updated, MORE efficient implementation

def LargestPalProduct2(numDigits):
    """
    Finds the largest palindrome made from the product of two 2-digit numbers.
    For example, the largest palindrome from two 2-digit numbers
    is 9009 = 91 × 99.
    NOTE: This is a more efficient/simple implementation of the function.
    """
    a = set()
    for i in range(smallestNum(numDigits), largestNum(numDigits)+1):
        for j in range(smallestNum(numDigits), largestNum(numDigits)+1):
            sum = i * j
            if isPal2(sum):
                a.add(sum)
    return max(a)

LargestPalProduct2(4)
