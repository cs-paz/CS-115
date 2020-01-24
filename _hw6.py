"""
Created on 10/26/19
@author: Christian Paz
Pledge: "I pledge my honor that I have abided by the Stevens Honor System."
 
CS115 - hw6
"""

# Each row has (x,y,carry-in) : (sum,carry-out)
FullAdder = {
('0','0','0') : ('0','0'),
('0','0','1') : ('1','0'),
('0','1','0') : ('1','0'),
('0','1','1') : ('0','1'),
('1','0','0') : ('1','0'),
('1','0','1') : ('0','1'),
('1','1','0') : ('0','1'),
('1','1','1') : ('1','1')
}

#returns string representing the number N in base B
def numToBaseB(N, B): 
    if (N == 0):
        return "0"
    return str(int(numToBaseB(int(N / B), B) + str(N % B)))

#takes input string S and base B and returns an integer in base 1-
def baseBToNum(S, B):
    if (S == ""):
        return 0
    return baseBToNum(S[:-1], B) * B + int(S[-1])

#returns string same number equivalent in base 2
def baseToBase(B1, B2, SinB1):
    return numToBaseB(baseBToNum(SinB1, B1), B2)

#returns sum of two binary strings
def add(S,T):
    return numToBaseB(baseBToNum(S, 2) + baseBToNum(T, 2), 2)

#adds two binary strings by converting both to base 10 and then reconverting at the end
def addB(S, T):
    delta = len(S) - len(T)
    if (delta > 0):
        T = "0" * delta + T
    if (delta < 0):
        S = "0" * delta + S
    def addBHelper(C, S, T):
        if (S == ""):
            if(C == "0"):
                return ""
            return "1"
        return addBHelper(FullAdder[(C, S[-1], T[-1])][1], S[:-1], T[:-1]) + FullAdder[(C, S[-1], T[-1])][0]
    return addBHelper("0", S, T)

#test cases
'''
print(numToBaseB(4,2)) #100
print(baseBToNum("11",2)) #3
print(baseToBase(2,10,"11")) #'3'
print(add("11","01")) #'100'
print(addB("11","1")) #'100'
'''
