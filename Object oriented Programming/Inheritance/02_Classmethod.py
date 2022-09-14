# class method use 

class Employee:
    a = 10
    b = 7
    c = 9

    @classmethod
    def setAttrs(cls,a,b,c):
        cls.a = a
        cls.b = b
        cls.c = c


emp = Employee()

print(Employee.a)
print(Employee.b)
print(Employee.c)

emp.setAttrs(1,2,4)

print(Employee.a)
print(Employee.b)
print(Employee.c)




    