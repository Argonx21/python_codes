import enum


list1 = [11,2,31,4,5,6,76,8,9,10]

for index,value in enumerate(list1):
    if (index+1 == 1 or index+1 == 3 or index+1 ==7):
        print(f"{index+1} => {value}")
