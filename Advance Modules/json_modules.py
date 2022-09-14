import json
import requests

# r = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=35&lon=139&appid=23ad6215867b43965ef67f9bbaf83c66")

# print(json.loads(r.text))
#json.loads method => parses json object in to python dict
#json.dumps method => converts python dictory content into actual json compatible format and return string as the output type
#json.dump method => is used for storing the json object to a file using write mode

# data = {
#     "name": ['gaurish','argon21'],
#     "bikes": None,
#     'cars': ('ferrari','bmw','tesla'),
#     'isHacker': False
# }

# print(json.dumps(data))

data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}

json_string = """
{
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}
"""
data1 = json.loads(json_string)
print(type(data1))
print(type(json.dumps(data)))
