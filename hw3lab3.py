'''
Created on 9/19/2019
@author:   Christian Szablewski-Paz 
Pledge:    I pledge my honor that I have abided by the Stevens Honor Code.

CS115 - Lab 3
'''
import sys
from cs115 import map, reduce, filter

def sum(x, y):
    return x+y

'''def change(amount, coins):
    if (amount == 0):
        return 0
    if (coins == [] or amount <= 0):
        return float("inf")
    else:
        loseIt = change(amount, coins[1:])
        useIt = 1 + change(amount - coins[0], coins)'''
        

def giveChange(amount, coins): # prints 
    if (amount == 0):
        return [0,[]]
    if (coins == [] or amount <= 0):
        return [float("inf"),[]]
    if (coins[0] > amount):
        return giveChange(amount, coins[1:])
    else:
        loseIt = giveChange(amount, coins[1:])
        useIt = giveChange(amount - coins[0], coins)
        useIt = [useIt[0]+1, useIt[1] + [coins[0]]]
        if(min(loseIt[0], useIt[0]) == loseIt[0]):
            return loseIt
        return useIt
        
'''print(change(48, [1, 5, 10, 25, 50]))'''
print(giveChange(48, [1, 5, 10, 25, 50]))
