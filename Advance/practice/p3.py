a=1
b=0

try:
    result = a/b
    print(f"The result of {a}/{b} is {result}")

except ZeroDivisionError:
    print("Infinite division exception")