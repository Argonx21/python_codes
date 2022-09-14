users1 = {"name":"Gaurish","age":24,"profession":"Hacker"}

print("Using items function => Prints both keys as well as values")
for i,val in users1.items():
    print("{} = {}".format(str(i),str(val)))

print("Using keys function => Prints key elements from dictionary")
for i in users1.keys():
    print("{}".format(str(i)))

print("Using values function => Prints every values associated with each key from dictionary")
for i in users1.values():
    print("{}".format(str(i)))
