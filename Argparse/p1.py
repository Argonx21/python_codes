import requests
import json
import argparse

parser = argparse.ArgumentParser(description='find garbage data here')
parser.add_argument('--id',metavar='id',type=str, help='Enter id')
args = parser.parse_args()

id = str(args.id)

print(id)

url = 'https://www.thesportsdb.com/api/v1/json/2/eventsseason.php?id='+id+'&s=2021-2022'
r = requests.get(url)
data=json.loads(r.text)
print(data['events'][0])