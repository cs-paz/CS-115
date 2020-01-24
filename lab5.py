'''
Created on _______________________
@author:   _______________________
Pledge:    _______________________

CS115 - Lab 5
'''
import time
from cs115 import map

words = []
HITS = 10
mem = {}

def fastED(first, second):
    '''Returns the edit distance between the strings first and second. Uses
    memoization to speed up the process.'''
    def fastEd_helper(first, second, m): #m = memory dictionary
        if (first, second) in m:
            return m[(first, second)]
        if first == '':
            final = len(second)
        elif second == '':
            final = len(first)
        elif first[0] == second[0]:
            final = fastED(first[1:], second[1:])
        else:
            s = 1 + fastEd_helper(first[1:], second[1:], m) #sub,del,ins
            d = 1 + fastEd_helper(first[1:], second, m)
            i = 1 + fastEd_helper(first, second[1:], m)
            final = min(s, d, i)
        m[(first, second)] = final
        return final
    return fastEd_helper(first, second, mem)
 
    

def getSuggestions(user_input): #w is a word in words[]
    '''For each word in the global words list, determine the edit distance of
    the user_input and the word. Return a list of tuples containing the
    (edit distance, word).
    Hint: Use map and lambda, and it's only one line of code!'''
    return map(lambda w: (fastED(user_input, w), w), words)

def spam():
    '''Main loop for the program that prompts the user for words to check.
    If the spelling is correct, it tells the user so. Otherwise, it provides up
    to HITS suggestions.

    To exit the loop, just hit Enter at the prompt.'''
    while True:
        user_input = input('spell check> ').strip()
        if user_input == '':
            break
        if user_input in words:
            print('Correct')
        else:
            start_time = time.time()
            suggestions = getSuggestions(user_input)
            suggestions.sort()
            endTime = time.time()
            print('Suggested alternatives:')
            for suggestion in suggestions[:HITS]:
                print(' %s' % suggestion[1])
            print('Computation time:', endTime - start_time, 'seconds')
    print('Bye')

if __name__ == '__main__':
    f = open('3esl.txt')
    for word in f:
        words.append(word.strip())
    f.close()
    spam()


print(fastED("xylophone", "yellow"))
