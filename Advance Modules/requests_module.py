import requests

r = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=35&lon=139&appid=23ad6215867b43965ef67f9bbaf83c66")

print(r.text)
print(r.status_code)

