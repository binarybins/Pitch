import requests
import json
import pandas as pd
import csv

yourapikey = "jEHXLRe13pKScLWAfz4dCSM1ADNPFRDeVEmJ5WtQ"
youremail = "tbm17160@hotmail.com"

# url = 'https://developer.nrel.gov/api/solar/nsrdb_data_query.json?api_key=jEHXLRe13pKScLWAfz4dCSM1ADNPFRDeVEmJ5WtQ&lat=1.371661&lon=103.823306'
# response = requests.get(url).json()

# print(json.dumps(response, indent = 1))


url = f"https://developer.nrel.gov/api/nsrdb/v2/solar/himawari-download.csv?\
names=2016&wkt=POINT%28103.823306+1.371661%29&interval=10&api_key={yourapikey}&email={youremail}"

response = requests.get(url)
# print(json.dumps(response, indent = 1))
print(response.text)

df = pd.read_csv(response)
df

# data = csv.reader(response)