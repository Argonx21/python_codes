# Multilevel inheritence and use of super method

class GrandParent:
    def __init__(self):
        print("Grand Parent")


class Parent(GrandParent):
    def __init__(self):
        super().__init__()
        print("Parent")



class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child")



ch = Child()

