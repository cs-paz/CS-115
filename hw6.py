'''
Created on 10/15/2019
@author:   Christian Szablewski-Paz
            Collaborated with Zac Schu
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

def completeFiveDigit(s):
    '''complete 5 digit if the binary string is not long enough, fill higher digits with 0.'''
    return "0" * (5 - len(s)) + s

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if (s == ""):
        return 0
    return binaryToNum(s[:-1]) * 2 + int(s[-1])

def compress(s):
    '''compress binary string and return compressed binary string'''
    def compress_helper(s, numInRow):
        '''return an array, whose members are arrays in format of ["0", 0], the first element indicates whether it is 1 or 0, the second element indicates the number of 1 or 0 existing consecutively.'''
        if (s == ""):
            return [numInRow]
        if (s[0] != numInRow[0] and numInRow[1] != 0):
                return [numInRow] + compress_helper(s[1:], [s[0]] + [1])
        return compress_helper(s[1:], [s[0]] + [numInRow[1] + 1])

    def compress_by_section(lst):
        '''accept result by compress_helper(), and return binary string translated from base 10. Split the number if the number of  consecutive 1 or 0 is larger than MAX_RUN_LENGTH'''
        if (lst == []):
            return ""
        if (lst[0][1] > MAX_RUN_LENGTH):
            return "1111100000" + compress_by_section([[lst[0][0]] + [lst[0][1]-31]] + lst[1:])
        return completeFiveDigit(numToBinary(lst[0][1])) + compress_by_section(lst[1:])

    return ("00000" if s[0] == "1" else "") + compress_by_section(compress_helper(s, ["0",0]))



def uncompress(s):
    '''return uncompressed binary'''
    def uncompress_by_section(s):
        '''uncompress binary and return a list of numbers of consecutive 0 and 1'''
        if s == "":
            return []
        return [binaryToNum(s[0:COMPRESSED_BLOCK_SIZE])] + uncompress_by_section(s[COMPRESSED_BLOCK_SIZE:]) # first arg +1

    def uncompress_helper(lst, zero):
        '''accept result from uncompress_by_section and produce the original binary string according to the array.'''
        if lst == []:
            return ""
        return ("0" if zero else "1" ) * lst[0] + uncompress_helper(lst[1:], not zero)

    return uncompress_helper(uncompress_by_section(s), True)


def compression(s):
    '''return the compression ratio of my compression algorithm'''
    return len(compress(s)) / len(s)

# Penguin
print(compression("00011000"+"00111100"*3 + "01111110"+"11111111"+"00111100"+"00100100"))
# Smile
print(compression("0"*8 + "01100110"*2 + "0"*8 + "00001000" + "01000010" + "01111110" + "0"*8))
# Five
print(compression("1"*9 + "0"*7 + "10000000"*2 + "1"*7 + "0" + "00000001"*2 + "1"*7 + "0"))

''' This compression algorithm works better if there are more consecutive 1 and 0. However, if there are more alternating 0 and 1, the compression rate is very low'''
