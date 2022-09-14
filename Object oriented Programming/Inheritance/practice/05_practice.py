# vector length calculate overloading
from termios import VLNEXT


class Vector:
    def __init__(self,vl):
        self.dim = len(vl)
        self.data = vl

    
    def __add__(self,obj):
        myList = []
        for i in range(len(obj.data)):
            myList.append(self.data[i]+obj.data[i])

        return Vector(myList)

    def __mul__(self,obj):
        dot = 0
        for i in range(len(obj.data)):
            dot += (self.data[i]*obj.data[i])
        return dot

v1 = Vector([1,2,3])
v2 = Vector([11,12,13])

v3 = v1 + v2
dotProduct = v1 * v2
print(f"Vector addition = {v3.data}")
print(f"Dot product = {dotProduct}")


