from os import name

from click import progressbar


class Programmer:
    def __init__(self,name,lang):
        self.name = name
        self.lang = lang

    def printOutput(self):
        print(f"Name = {self.name}  Language = {self.lang}")


gaurish = Programmer("Gaurish","Python")
argon = Programmer("Argon21","golang")

gaurish.printOutput()
argon.printOutput()