# Class and instance attributes 

class Employee:
    name = "lol"
    title = "Manager"
    salary = "50k"
    # All these attributes are class attributes


jack = Employee()
# all below mentioned attributes are known as instance attributes

jack.name = "Jack Gralish"
jack.title = "Consultant"
jack.salary = "90k"

print(f"Title: {jack.title}\nName: {jack.name}\nSalary: {jack.salary}")

silva = Employee()
print(f"Title: {silva.title}\nName: {silva.name}\nSalary: {silva.salary}")
# The above statement will first check if the instance has a instance variable values defined in it, if not then it will take the values from the parent class

#Instance attribute has more preference compared to class attribute
