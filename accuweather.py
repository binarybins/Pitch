import requests
import json

###some comments###
###desktop comments###

lat = 1.371661
lon = 103.823306
API_key = 'mtPjpsrWZZXFco9TtddtQAv0PVtvql3s'
loc_key = 300597

url = f'http://dataservice.accuweather.com/currentconditions/v1/{loc_key}?apikey={API_key}&details=true'


response = requests.get(url).json()
#print(response.text)
print(json.dumps(response, indent = 1))

