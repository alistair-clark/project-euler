'''
Project Euler
Problem #18: Maximum path sum I

By starting at the top of the triangle below and moving to adjacent numbers on the row below,
the maximum total from top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route.
However, Problem 67, is the same challenge with a triangle containing one-hundred rows;
it cannot be solved by brute force, and requires a clever method! ;o)

Date: May 25, 2019
'''

# Import packages needed to scrape Project Euler site
import requests
from bs4 import BeautifulSoup

# Scrape url page
url = "https://projecteuler.net/problem=18"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

# Pull text of pyramid of numbers and convert into list of lists with ints
selector = '.problem_content p:nth-child(5)' # Found using "Inspect" on webpage
pyramidText = soup.select_one(selector).text.splitlines() # Select text and split on new lines
pyramidText = [s.split(' ') for s in pyramidText] # Split long strings into individual strings for each number
pyramidNums = [list(map(int, row)) for row in pyramidText] # Convert each string into an int

# Start at the bottom, adding pairs of numbers
row = len(pyramidNums)-2
while row >= 0:
    for num in range(len(pyramidNums[row])):
        pyramidNums[row][num] = pyramidNums[row][num] + max(pyramidNums[row+1][num], pyramidNums[row+1][num+1])
    row -=1
pyramidNums[0][0]
