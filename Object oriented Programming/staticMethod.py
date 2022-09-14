# if a method present inside a class does not required self or any object then we can mark it as a static method using decorator

class Employee:
    name = "test"
    salary = "40k"

    def printObject(self):
        print(f"{self.name} and {self.salary}")

    
    @staticmethod       # used for marking a method as a static
    def greet():
        print("Welcome to the club!")

# using instance/object
kevin = Employee()
kevin.greet()
kevin.printObject()

# using class variables

Employee.greet()
Employee.printObject(kevin)