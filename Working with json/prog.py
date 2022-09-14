import json

book = {}
book["user1"] = {
    "name": "Gaurish",
    "address": "test addr",
    "phone_num": 1234567890
}

book["user2"] = {
    "name": "Argon",
    "address": "addr test",
    "phone_num": 12345454590
}

data = json.dumps(book)
print(type(data))

with open("data.txt","w") as f:
    f.write(data)