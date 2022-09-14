number = int(input("Enter a number to print it's multiplication table:"))

data = [i* number for i in range(1,11)]

print(f"Multiplication table for {number}:")
for d in data:
    print(d)