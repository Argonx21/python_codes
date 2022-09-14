import math


class Calculator:
    def __init__(self,number):
        self.number =  number


    def square(self):
        return self.number**2
    
    def cube(self):
        return self.number**3
    
    def squareRoot(self):
        return math.sqrt(self.number)



cal = Calculator(64)

print(cal.square())
print(cal.cube())
print(cal.squareRoot())


