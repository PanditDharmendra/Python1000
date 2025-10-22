class Calculator:
    @staticmethod
    def __init__(n):
        n = n 
        
    @staticmethod
    def Square(n):
         print("The sqaure", n*n)

    @staticmethod
    def Cube (n):
        print("The Cube is", n*n*n)

    @staticmethod
    def SquareRoot(n):
        print("The SquareRoot is ",n**1/2)

a = Calculator(5)
a.Square(5)
a.SquareRoot(5)
a.Cube(5)
