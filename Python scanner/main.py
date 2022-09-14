import requests
import json

x = requests.get("http://evil.com")

headers = x.headers
print(headers['server'])