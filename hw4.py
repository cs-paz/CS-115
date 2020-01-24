'''
Created on 10/10/19
@author:   Christian Szablewski-Paz
Pledge:    I pledge my honor that I have abided by Stevens Honor System.

CS115 - Hw 5
'''
#changing this import made it easier so I didn't have to reference turtle every time

from turtle import *

def snowflake(trunk_length, levels): #draws equilateral triangle
    speed(1000)
    penup()
    goto(-200,100)
    pendown()
    #above code is unneccesary but made the snowflake more pretty and centered
    
    for i in range(3):
        snowflakeSide(trunk_length, levels) 
        right(120)
    
# Ignore 'Undefined variable from import' errors in Eclipse.

def snowflakeSide(trunk_length, levels):
        if (levels == 0):
            forward(trunk_length)
        else:
            snowflakeSide(trunk_length/3, levels - 1)
            left(60)
            snowflakeSide(trunk_length/3, levels - 1)
            right(120)
            snowflakeSide(trunk_length/3, levels - 1)
            left(60)
            snowflakeSide(trunk_length/3, levels - 1)

def fast_change(amount, coins):
    '''Takes an amount and a list of coin denominations as input.
    Returns the number of coins required to total the given amount.
    Use memoization to improve performance.'''
    def fast_change_helper(amount, coins, memo):
        if ((amount, coins) in memo):
            return memo[(amount, coins)]
        if (amount == 0):
            final = 0
        elif (amount < 0 or len(coins) == 0):
            final = float("inf")
        else:
            useIt = 1 + fast_change_helper(amount - coins[0], coins, memo)
            loseIt = fast_change_helper(amount, coins[1:], memo)
            if(loseIt == 0):
                final = min(useIt, float("inf"))
            final = min(useIt, loseIt)
        memo[(amount, coins)] = final
        return final
    
    return fast_change_helper(amount, tuple(coins), {})

# If you did this correctly, the results should be nearly instantaneous.
print(fast_change(131, [1, 5, 10, 20, 50, 100]))
print(fast_change(292, [1, 5, 10, 20, 50, 100]))
print(fast_change(673, [1, 5, 10, 20, 50, 100]))
print(fast_change(724, [1, 5, 10, 20, 50, 100]))
print(fast_change(888, [1, 5, 10, 20, 50, 100]))

# Should take a few seconds to draw a snow flake
snowflake(400, 4)

