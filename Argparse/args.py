def addition(*args):
    sum = 0
    for param in args:
        sum += param
    
    return sum

#print(addition(1,2,3,4,5))

# *args can pass undefined number of positional arguments within a tuple
# **kwargs (keyword arguments) can pass undefined number of key value pair arguments inside a dict 

def name_builder(**kwargs):
    print("Hello",end=" ")
    for k,v in kwargs.items():
        print(v,end=" ")

name_builder(first="Gaurish",mid="C",last="Kauthankar")
