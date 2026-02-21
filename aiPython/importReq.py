import requests
import json

url = 'http://ip-api.com/json/'
params = {
'status': 'status',
'city': 'city',
'regionName': 'regionName',
'zip': 'zip',
'isp': 'isp',
'org': 'org'
}
response = requests.get(url, params=params).json()

print('=' * 30)
print(f"Request status -- {response['status']}")
print(f"City -- {response['city']}")
print(f"State -- {response['regionName']}")
print(f"Zip -- {response['zip']}")
print(f"Internet Provider -- {response['isp']}")
print(f"ISP Organization -- {response['org']}")
print(f"Host IP -- {response['query']}")
print('=' * 30)

