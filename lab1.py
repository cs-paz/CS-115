""""Christian Szablewski-Paz""""
""""cszablew""""
""""I pledge my honor that I have abided by the Stevens Honor System.
	Christian S. Szablewski-Paz
""""
from cs115 import map, reduce, functools
import math
from math import *

def inverse(x):
    return (1/x)

def sum(x,y):
    return(x+y)

def e(n):
   x = map(factorial, range(1, n+1))
   y = reduce(sum, map(inverse, x)) + 1
   return (y)

def error(n):
    x = math.e - e(n)
    return abs(x)





