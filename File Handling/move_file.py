import os

src = "temp_file.txt"
dst = "/home/user/Desktop/temp_file.txt"

try:
    if os.path.exists(dst):
        print("File already present")
    else:
        os.replace(src,dst)
        print(src+" was moved to "+dst)

except FileNotFoundError:
    print(src + " was not found")