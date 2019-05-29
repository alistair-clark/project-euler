'''
Project Euler:
Problem #22: Names scores

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

Date: May 29, 2019
'''

# read text file into pandas dataframe, and
import pandas as pd
import string
names_df = pd.read_csv('p022_names.txt', header=None).transpose()

# add column name
names_df.columns = ['Name']
names_df['Score'] = ''
names_df['Rank'] = ''
names_df['Total'] = ''
names_df.set_index('Name',inplace=True)

# sort alphabetically and drop NaN row
names_df = names_df.sort_values(by=['Name'])
names_df.head(5)
names_df.tail(5)
names_df.drop(names_df.tail(1).index,inplace=True)
names_df.drop(axis=0,index='NAN',inplace=True) # Drop NaN name
names_df.info()

# create alphabet scoring dict
alphabet = {}
for letter in string.ascii_uppercase:
    alphabet[letter] = string.ascii_uppercase.index(letter) + 1

# add 'Score' to dataframe
for i, row in names_df.iterrows():
    sum = 0
    for letter in i:
        sumLetters = 0
        sum += alphabet[letter]
    names_df.at[i, 'Score'] = sum

# add 'Rank' to dataframe
rank = 1
for i, row in names_df.iterrows():
    names_df.at[i, 'Rank'] = rank
    rank += 1

# add 'Total' to dataframe
for i, row in names_df.iterrows():
    names_df.at[i, 'Total'] = names_df.at[i, 'Score'] * names_df.at[i, 'Rank']

# sum the total for all names (off by a bit, not sure why)
totalscore = names_df['Total'].sum()
print(totalscore)
