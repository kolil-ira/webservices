import json


json_data = '''
{
  "name": "ira kip",
  "age":19,
  "address": {
    "street": "parklands",
    "city": "Nairobi"
  },
  "phoneNumbers": ["123-456-7890", "997-60-3210"]
}
'''


data = json.loads(json_data)


name = data['name']
address = data['address']['city']
phone_numbers = data['phoneNumbers']

print(f"Name: {name}")
print(f"City: {address}")
print(f"Phone Numbers: {', '.join(phone_numbers)}")
