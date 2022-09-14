# program to compute salary after increment using property decorator

class Employee:
    def __init__(self,salary,inc):
        self.salary = salary
        self.inc = inc 

    @property
    def salaryAfterInc(self):
        return self.salary * (1+self.inc)

    @salaryAfterInc.setter  # setter decorator
    def salaryAfterInc(self):
        self.salary = self.salary * (1+self.inc)



emp1 = Employee(12000,0.1)

print(emp1.salaryAfterInc)

emp1.salaryAfterInc = 15000

print(emp1.salaryAfterInc)