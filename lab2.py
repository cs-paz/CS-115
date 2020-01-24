
"""Christian Szablewski-Paz
cszablew
I pledge my honor that I have abided by the Stevens Honor System.
	Christian S. Szablewski-Paz"""
from cs115 import map, reduce

def dot(L, K):
    if (L == [] or K == []):
        return 0
    return (L[0]*K[0] + dot(L[1:], K[1:]))

x1 = [1, 2, 3]
x2 = [1, 2, 3]

def explode(S):
    if (len(S) != 0):
        return [S[0]] + explode(S[1:])
    return []

def ind(e, L):
    if not L:
        return 0
    if(L[0] == e):
        return 0
    return(1 + ind(e,L[1:]))

def removeAll(e, L):
    if (e in L):
      list1 = L
      list1.remove(e)
      return (removeAll(e, list1))
    else:
        return L

def myFilter(f, L):
    if (L ==[]):
        return []
    if f(L[0]):
        return [L[0]] + myFilter(f, L[1:])
    else:
        return myFilter(f, L[1:])

def deepReverse(L):
    if (L == []):
        return []
    if isinstance(L[len(L)- 1], list):
        return [deepReverse(L[len(L) -1])] + deepReverse(L[:-1])
    else:
        return [L[-1]] + deepReverse(L[:-1])

"""Test Cases"""
print(dot(x1,x2))
print(explode("Spam"))
print(ind(42, [ 55, 77, 42, 12, 42, 100 ]))
print(removeAll(1,[1,2,3,1,4,5,1]))


"""4 3 2 1 0 (negative)
   0 1 2 3 4 (positive
   w h i t e      """                             
