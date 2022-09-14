data = ["test","data","nano","hackers"]

#enumerate function makes enumeration by iterating through the list , the first value is the index value and the second value is the actual data which is stored in the list.


for i,value in enumerate(data):
    print("Index {} has value={}".format(str(i),value))

for value in data:
    print(value)