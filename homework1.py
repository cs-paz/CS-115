"""Christian Szablewski-Paz
cszablew
I pledge my honor that I have abided by the Stevens Honor System.
	Christian S. Szablewski-Paz"""
from cs115 import map, reduce

def mult(x, y):
    return x*y

def sum(x, y):
    return x+y

def factorial(n):
    return(reduce(mult, range(1, n+1)))

def mean(L):
    total = reduce(sum, L)
    return (total/len(L))

def divides(n):
    def div(k):
        return n % k == 0
    return div

def prime(n):
    return True not in (map(divides(n), range(2,n)))

"""Test Cases"""

list1 = [1, 2, 3]
list2 = [1, 2, 3, 4, 5]
list3 = [1, 2, 3, 4, 5, 6, 7]

print(factorial(5))
print(factorial(3))
print(factorial(4))
print(mean(list1))
print(mean(list2))
print(mean(list3))

if (prime(9)):
    print ("This number is prime")
else:
    print("This number is not prime")

if (prime(17)):
    print ("This number is prime")
else:
    print("This number is not prime")




