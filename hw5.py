'''
Created on 10/15/2019
@author:   Christian Szablewski-Paz
            Collaborated with Zac Schuh
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.
                CS.Paz

CS115 - Hw 5
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if (n == 0):
        return ""
    return numToBinary(int(n / 2)) + str(n%2)

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if (s == ""):
        return 0
    return binaryToNum(s[:-1]) * 2 + int(s[-1])

def toFiveDigits(s):
    '''runs if the string isnt long enough, fills the higher digits w zero'''
    return "0" * (5 - len(s)) + s

def compress(s):
    '''returns compressed binary string'''
    def compress_helper1(s, numInRow):
        '''returns list in the format ["1 or 0", HowManyConsecutive]'''
        if (s == ""):
            return [numInRow]
        if (s[0] != numInRow[0] and numInRow[1] != 0):
                return [numInRow] + compress_helper1(s[1:], [s[0]] + [1])
        return compress_helper1(s[1:], [s[0]] + [numInRow[1] + 1])

    def compress_helper2(lst):
        '''returns binary string translated from base 10. '''
        if (lst == []):
            return ""
        if (lst[0][1] > MAX_RUN_LENGTH):
            return "1111100000" + compress_helper2([[lst[0][0]] + [lst[0][1]-31]] + lst[1:])
        return toFiveDigits(numToBinary(lst[0][1])) + compress_helper2(lst[1:])

    if(s[0] == "1"):
        return "00000" + compress_helper2(compress_helper1(s, ["0",0]))
    else:
        return "" + compress_helper2(compress_helper1(s, ["0",0]))

def uncompress(s):
    '''returns uncompressed binary string'''
    def uncompress_helper1(s):
        if (s == ""):
            return []
        return [binaryToNum(s[0:COMPRESSED_BLOCK_SIZE])] + uncompress_helper1(s[COMPRESSED_BLOCK_SIZE:]) 

    def uncompress_helper2(lst, z): #sub uncompress
        if (lst == []):
            return ""
        if (z):
            return "0" * lst[0] + uncompress_helper2(lst[1:], not z)
        else:
            return "1" * lst[0] + uncompress_helper2(lst[1:], not z)
        
    return uncompress_helper2(uncompress_helper1(s), True)


def compression(s):
    return len(compress(s)) / len(s)

'''
print(compression("00011000"+"00111100"*3 + "01111110"+"11111111"+"00111100"+"00100100")) # Penguin
print(compression("0"*8 + "01100110"*2 + "0"*8 + "00001000" + "01000010" + "01111110" + "0"*8)) # Smile
print(compression("1"*9 + "0"*7 + "10000000"*2 + "1"*7 + "0" + "00000001"*2 + "1"*7 + "0"))# Five
print(compression("0"*4 + "01100110"*1 + "0"*4 + "00001000" + "01000010" + "01111110" + "0"*4)) #messed up smile
print(compression("0"*16 + "1"*16 + "0"*16 + "1"*16)) #white,black,white,black
#for test cases
print(compress("1"*64))
print(compression("1"*64))
print(compress("0111" * 16))
print(compression("0111" * 16))
'''

''' The algorithm works better with more consecutive numbers in a row, or else the speed will be slow'''
