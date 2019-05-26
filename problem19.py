'''
Project Euler
Problem #19: Counting Sundays

You are given the following information, but you may prefer to do some research for yourself.

 - 1 Jan 1900 was a Monday.
 - Thirty days has September,
   April, June and November.
   All the rest have thirty-one,
   Saving February alone,
   Which has twenty-eight, rain or shine.
   And on leap years, twenty-nine.
 - A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

Date: May 26, 2019
'''
# Find total days between 1 Jan 1901 to 31 Dec 2000
daysInYear = 365
daysInLeapYear = 366
years = [i for i in range(1901,2001)]
days = [daysInYear if year % 4 != 0 else daysInLeapYear for year in years ]
totalDays = sum(days)

# create list of Sundays
sundays = [sunday for sunday in range(1,totalDays) if sunday % 7 == 0]
sundays = [i-1 for i in sundays] # adjusting because first Sunday occurs on the 6th day in 1901

# Create list of first of the month
firstOfMonthNonLeap = [1, 32, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
firstOfMonthLeap = [1, 32, 61, 92, 122, 153, 183, 214, 245, 275, 306, 336]
firstOfMonth = []
counter = 0
for year in days:
    if year == 365:
        for day in firstOfMonthNonLeap:
            firstOfMonth.append(counter + day)
        counter += year
    elif year == 366:
        for day in firstOfMonthLeap:
            firstOfMonth.append(counter + day)
        counter += year
    else:
        Print('error')

# Turn two lists into sets and find the intersection
x = set(sundays)
y = set(firstOfMonth)
z = set(x) & set(y)
len(z)
