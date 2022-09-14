#Traditional operators can be overloaded using dunder method



class Addition:
    def __init__(self,a):
        self.a = a
    
    def __add__(self,obj):
        return self.a + obj.a


a = Addition(45)
b = Addition(40)

print(a + b)
