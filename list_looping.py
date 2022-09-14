name = ["Gaurish","bhavde","Subzero"]
age = [23,24,25]

for n,a in zip(name,age):
    print(f"name = {n} and age = {a}")

for n in name:
    print(f"{n} ==> {name.index(n)}")


newList = [2,4,5,61,1,0,21]
newList.sort(reverse=True)
print(newList)