import shutil as cp 

# shutil module has copyfile(), copy() and copy2() methods which could be used to perform copy operation on a file.
# This will copy file including its content as well as its meta data.

cp.copyfile("data.txt","/home/user/Desktop/new_data.txt")