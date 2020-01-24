'''
Created on 9/25/2019
@author:   Christian Szablewski-Paz 
Pledge:    I pledge my honor that I have abided by the Stevens Honor Code.

CS115 - Hw 3
'''
# Be sure to submit hw3.py.  Remove the '_template' from the file name.

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# your code goes here

def giveChange(amount, coins): # prints list of minimum number of coins and their values as well as the length of the list
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

print(giveChange(48, [1, 5, 10, 25, 50]))

x = "hello"
print(x[1:])
print(x[1:3])
      
