import requests
import json

lat = 1.371661
lon = 103.823306
API_key = 'c8c4b3dac012316a26b7f8254bccd8b6'

url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric&hourly'

###5 day / 3 hour forecast data https://openweathermap.org/forecast5 ###
forecast = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_key}'

response = requests.get(url).json()
print(json.dumps(response, indent = 1))


# # Serializing json
# json_object = json.dumps(response, indent=4)

# # Writing to sample.json
# with open("sample.json", "w") as outfile:
#     outfile.write(json_object)
