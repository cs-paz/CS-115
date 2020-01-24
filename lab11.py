import math

class QuadraticEquation:

    def __init__(self, A, B, C): #constructor
        try:
           self.a = float(A)
        except  ValueError:
            print("Coefficient 'a' cannot be 0 in a quadratic equation")    
        self.b = float(B)
        self.c = float(C)

    @property
    def a(): 
        return a

    @property
    def b(): 
        return b

    @property
    def c():
        return c

    def discriminant(): #returns discriminant
        return (b*b) - (4*a*c)

    def root1():
        return (((b*(-1)) + math.sqrt((b*b) - (4*a*c)))/(2*a))

    def root2():
        return (((b*(-1)) - math.sqrt((b*b) - (4*a*c)))/(2*a))
        
    def __str__(): #returns ax^2 + bx + c
        if(a > 0):
            ax = str(a) + "x^2"
        else:
            ax = "-" + str(a) + "x^2"                
        if(b != 0):
            if (b > 0):
                bx = str(b) + "x"
            elif (b < 0):
                bx = "-" + str(b) + "x"
            else:
                bx = ""                
        if(c != 0):
            if (c > 0):
                cx = str(c)
            elif (c < 0):
                cx = "-" + str(c)
            else:
                cx = ""

            return ax + " " + bx + " " + cx

            
'''if __name__=="__main__":
    x = QuadraticEquation(1.0, 4.0, 4.0)
    print("root1:" + x.root1())
    print("root2:" + x.root2())'''

