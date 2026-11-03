import requests

base_url = 'http://localhost:8080'

response = requests.get(f'{base_url}/cars/prices').json()
response2 = requests.get(f'{base_url}/cars').json()
response3 = requests.get(f'{base_url}/manufacturers').json()

print(response3)