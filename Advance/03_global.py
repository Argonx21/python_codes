# use of global keyword in python

from re import A


a = 10

def function():
    global a # global keyword is used to directly modify the variable a which is out side of the functions scope. and any changes to its value will update the variable a's value globally.
    a = 8
    print(a)
    a = 100
    print(a)

print(a)
function()
print(a)