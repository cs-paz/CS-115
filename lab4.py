'''
Created on 9/19/2019
@author:   Christian Szablewski-Paz 
Pledge:    I pledge my honor that I have abided by the Stevens Honor Code.

CS115 - Lab 3
'''

import sys
from cs115 import map, reduce, filter

def coin_row(L):
    if not L:
        return 0
    useIt = L[0] + coin_row(L[2:])
    loseIt = coin_row(L[1:])
    return max(loseIt, useIt)

def coin_row_with_values(L):
    if not L:
        return [0, []]
    useIt = [L[0] + coin_row_with_values(L[2:])[0], [L[0]] + coin_row_with_values(L[2:])[1]]
    loseIt = coin_row_with_values(L[1:])
    if useIt[0] > loseIt[0]:
        return useIt
    else:
        return loseIt

def countIf(f,L)
    if not L:
        return 0
    head, tail = L[0], L[1:]
    headContribution = 1 if f(head) else 0
    return headContribution + countIf(f, tail)

def m

print(coin_row([]))
print(coin_row_with_values([]))
print(coin_row([5, 1, 2, 10, 6, 2]))
print(coin_row_with_values([5, 1, 2, 10, 6, 2]))
print(coin_row([10, 5, 5, 5, 10, 50, 1, 10, 1, 1, 25]))
print(coin_row_with_values([10, 5, 5, 5, 10, 50, 1, 10, 1, 1, 25]))
