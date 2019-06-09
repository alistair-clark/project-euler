'''
Project Euler:
Problem #31: Coin sums

In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:
    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?

Date: June 9, 2019
'''

#Solved using dynamic programming
def coinCombos(coins, numCoins, target):
    """
    Assumes coins is a list, numCoins is a positive integer that equals the length of the coins list, and target is a positive integer.

    Returns the number of different ways the target can be created from the coins in the list.
    """
    # create a blank list from 0 to target that we'll use to count how many ways to make change for each number up to the target (1, 2, 3, ..., target)
    table = [0 for x in range(target+1)]
    # base case if the target is 0
    table[0] = 1
    # iterate through each coin and update the table for every index above the coin picked
    for i in range(0,numCoins):
        for j in range(coins[i],target+1):
            table[j] += table[j-coins[i]]
            print(table[j])
    return table[target]

target = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]
numCoins = len(coins)
coinCombos(coins, numCoins, target)
