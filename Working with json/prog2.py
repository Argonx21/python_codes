import json

with open("./data.txt","r") as f:
    s = f.read()

data = json.loads(s)
test = ["test","sfdsf","dfdfdadf","dfadfdf","etest"]

for data in test:
    print(data)

for d in data:
    print(data[d])