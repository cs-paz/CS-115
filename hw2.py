'''
Created on 9/19/2019
@author:   Christian Szablewski-Paz - collaborated with Zac Schuh
Pledge:    I pledge my honor that I have abided by the Stevens Honor Code.
                Christian Szablewski-Paz

CS115 - Hw 2
'''
import sys
from cs115 import map, reduce, filter

sys.setrecursionlimit(10000)
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]
Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

def sum(x,y): #returns sum
    return (x + y)

def removeX(x, Rack): #removes letter x from the list
    if (Rack == []):
        return []
    if (Rack[0] == x):
        return Rack[1:]
    return [Rack[0]] + removeX(x, Rack[1:])

def isValid(x, Rack): #returns whether the specific string combination is a valid word in the global dictionary
    if (Rack == [] and len(x) > 0):
        return False
    elif (len(x) == 0):
        return True
    if not (x[0] in Rack):
        return False
    return isValid(x[1:], removeX(x[0], Rack))

def letterScore(letter, scorelist): #returns score associated with that letter
    if(scorelist[0][0] == letter):
        return scorelist[0][1] 
    else:
        return filter(lambda x: x[0] == letter, scorelist)[0][1]


def wordScore(S, scorelist): #returns the total score of all of the characters in the list
    if(S == ""):
        return 0
    else:
        return(letterScore(S[0], scorelist) + wordScore(S[1:], scorelist))

def scoreList(Rack): #returns a list of all of the words from the global dictionary that can be made as well as their scoress
    def subScoreList(D,Rack):
        if not D:
            return []
        if isValid(D[0],Rack):
            return [[D[0], wordScore(D[0],scrabbleScores)]]+subScoreList(D[1:], Rack)
        else:
            return subScoreList(D[1:],Rack)
    return subScoreList(Dictionary,Rack)

def bestWord(Rack): #returns the highest scoring word from the scoreList function
    def subBestWord(L, word):
        if not L:
            return word
        if L[0][1] >= word[1]:
            return subBestWord(L[1:], L[0])
        else:
            return subBestWord(L[1:], word)
    return subBestWord(scoreList(Rack), ['', 0])
    
#small test cases
print(letterScore("c", scrabbleScores))
print(wordScore("spam", scrabbleScores))
print(bestWord(["a", "am"]))
