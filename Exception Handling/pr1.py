# Checking if the entered values throws error related to the values or division by zero


try:
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    print(a/b)

except ValueError:
    print("Value error occured")

except Exception as e:
    print(f"This is the error: {e}")

    