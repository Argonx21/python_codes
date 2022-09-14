# generate tables and store each table inside a seperate files in tables folder

for number in range(10,21):
    filename = f'tables/{number}_table.txt'
    # print(filename)
    with open(filename,"a") as f:
        for counter in range(1,11):
            data = f"{number}*{counter}  = {(number*counter)}\n"
            f.write(data)
