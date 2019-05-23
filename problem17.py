'''
Project Euler
Problem #17: Number letter counts


If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.

Date: May 23, 2019
'''

def num2words(num):
    """
    Function takes an integer input and returns the number written out in words as a string

    For example, the numbers 1 to 5 written out in words: one, two, three, four, five.
    """
    # Create a dictionary of all unique numbers from 1 to 1,000
    num2words = {0:'', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven',\
    8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen',\
    15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty',\
    30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty',\
    90:'ninety', 1000:'onethousand'}
    result = ''
    while True:
        try:
            result += num2words[num]
            return result
        except:
            pass
        try:
            result += num2words[num-num%10] + num2words[num%10]
            return result
        except:
            result += num2words[(num - num%100)//100] + 'hundred'
            num = num%100
            if num == 0:
                return result
            else:
                result += 'and'

def numLetterCount(maxNum):
    """
    Function returns the number of letters used to write out the numbers from
    1 to maxNum
    """
    sum = 0
    for num in range(1,maxNum+1):
        sum += len(num2words(num))
        print(str(num) + ' = ' + str(num2words(num)))
    return sum

numLetterCount(1000)
