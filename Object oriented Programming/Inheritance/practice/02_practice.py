class Animals:
    def __init__(self):
        pass

class Pets(Animals):
    def __init__(self):
        pass

class Dog(Pets):
    def __init__(self):
        super().__init__()

    @staticmethod
    def bark():
        print("Bark")


