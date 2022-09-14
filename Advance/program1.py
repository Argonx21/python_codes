# program to understand the actual meaning of __name=="__main__"

def function():
    print("This is a function from program1 module")



print(__name__) 
# value of __name__ will be __main__ only if this file is executed and in return the condition will be true resulting in making a function call to the function.
# if some other program wants to use this function after importing this module, then in that case the value of the __name__ will be this modules name and function will not be called.
if __name__ == "__main__": 
    function()
    