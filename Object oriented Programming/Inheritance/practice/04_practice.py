# program to add and multiply complex numbers using operator overloading
class Complex:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    
    def __add__(self,obj):
        return Complex(self.a + obj.a, self.b + obj.b)


c1 = Complex(1,2)
c2 = Complex(12,13)

c3 = c1 + c2
print(c3.a, c3.b)
