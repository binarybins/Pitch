import requests
import json
url = 'https://data.gov.sg/api/action/datastore_search?resource_id=1e478275-0746-483d-9783-2f40a3535910&limit=5'


response = requests.get(url).json()
#print(response.text)
print(json.dumps(response, indent = 1))

