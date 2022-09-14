# Constructor demonstration in python OOPs

from curses.ascii import EM
from os import name
from symtable import SymbolTableFactory


class Employee:
    company = "Unknown"     # Class attribute
    def __init__(self,name="test User",salary="20k",company="testcorp"):
        # instance attributes
        self.name = name
        self.salary = salary
        self.company = company

    def printObject(self):
        print(f"Name = {self.name}\nSalary = {self.salary}\nCompany = {self.company}")



gaurish = Employee()
gaurish.printObject()
argon = Employee("argon","80K","test")
argon.printObject()