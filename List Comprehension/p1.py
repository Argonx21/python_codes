
# List Comprehension
a = [1,3,5,4,7,8]

data = [i+3 for i in a]
print(data)



# Dictionary comprehension

dict1 = {i:f"Item {i}" for i in range(10)}
print(dict1)

# reversing values of dictionary using comprehension method
dict1 = {value:key for key,value in dict1.items()}
print(dict1)