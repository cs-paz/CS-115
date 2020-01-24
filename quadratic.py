import math

class QuadraticEquation(object):

    def __init__(self, A, B, C): #constructor
        if A == 0:
            raise ValueError("Coefficient 'a' cannot be 0 in a quadratic equation.")
            return
        self.__a = float(A) 
        self.__b = float(B)
        self.__c = float(C)

    @property
    def a(self): 
        return self.__a

    @property
    def b(self): 
        return self.__b

    @property
    def c(self):
        return self.__c

    def discriminant(self): #returns discriminant
        return (self.__b ** 2) - (4*self.__a*self.__c)

    def root1(self):
        if self.discriminant() < 0:
            return None
        return ((- self.__b + math.sqrt(self.discriminant())) / (2 * self.__a))

    def root2(self):
        if self.discriminant() < 0:
            return None
        return ((- self.__b - math.sqrt(self.discriminant())) / (2 * self.__a))
    
    def __str__(self): #returns ax^2 + bx + c
        ax = str(self.__a)
        bx = str(self.__b)
        cx = str(self.__c)

        if abs(self.__a) == 1.0:
            ax = "x^2 " if self.__a > 0 else "-x^2 "
        else:
            ax = (ax if self.__a > 0 else "- " + ax[1:]) + "x^2 "

        if abs(self.__b) == 1.0:
            bx = "+ x " if self.__b > 0 else "- x "
        elif self.__b == 0:
            bx = ""
        else:
            bx = ("+ " + bx if self.__b > 0 else "- " + bx[1:]) + "x "

        if abs(self.__c) == 1.0:
            cx = "+ 1.0 " if self.__c > 0 else "- 1.0 "
        elif self.__c == 0:
            cx = ""
        else:
            cx = ("+ " + cx if self.__c > 0 else "- " + cx[1:]) + " "

        return ax + bx + cx + "= 0"


            
'''if __name__=="__main__":
    x = QuadraticEquation(1.0, 4.0, 4.0)
    print("root1:" + x.root1())
    print("root2:" + x.root2())'''

