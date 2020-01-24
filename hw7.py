def TcToNum(s): #  8 bits representing an integer in two's-complement, and returns the corresponding integer  
    def TcToNum_Helper(s):
        if (s == ""):
            return 0
        return TcToNum_Helper(s[:-1]) * 2 + int(s[-1])
    '''main function below'''
    if(s[0] == "0"):
        return TcToNum_Helper(s[1:])
    else:
        return TcToNum_Helper(s[1:]) - 128

def NumToTc(n):
    '''helper functions numToBinary and completeSevenDigits'''
    def numToBinary(n):
        '''Precondition: integer argument is non-negative.
        Returns the string with the binary representation of non-negative integer n.
        If n is 0, the empty string is returned.'''
        if (n == 0):
            return ""
        return numToBinary(int(n / 2)) + str(n%2)
    
    def completeSevenDigit(s): # complete 7 digit if the binary string is not long enough, fill higher digits with 0
        return "0" * (7 - len(s)) + s
    '''main function is below'''
    if (n >= 128 or n < -128):
        return 'Error'
    if (n >= 0):
        return "0" + completeSevenDigit(numToBinary(n))
    else:
        return "1" + completeSevenDigit(numToBinary(n + 128))

'''test functions'''
print(TcToNum("00000001"))
print(TcToNum("11111111"))
print(TcToNum("10000000"))
print(TcToNum("01000000"))
print(NumToTc(1))
print(NumToTc(-128))
print(NumToTc(200))
