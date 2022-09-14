s = {} #this is a wrong way of creating a set
print(type(s))

# to create a set use below Syntax 
set1 = set()
print(type(set1))



# set stores non repitative values inside it.
set1 = {1,2,3,4,5,1,2,4}

print(set1)

set1.add(23) # adding a new element inside the set
print(set1)
set1.remove(5) # removing an element from the set
print(set1)


