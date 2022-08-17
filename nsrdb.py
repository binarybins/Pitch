import requests
import json
import pandas as pd
import csv

yourapikey = "jEHXLRe13pKScLWAfz4dCSM1ADNPFRDeVEmJ5WtQ"
youremail = "tbm17160@hotmail.com"

# url = 'https://developer.nrel.gov/api/solar/nsrdb_data_query.json?api_key=jEHXLRe13pKScLWAfz4dCSM1ADNPFRDeVEmJ5WtQ&lat=1.371661&lon=103.823306'
# response = requests.get(url).json()

# print(json.dumps(response, indent = 1))

url_2016 = "https://developer.nrel.gov/api/nsrdb/v2/solar/himawari-download.csv?names=2016&wkt=POINT%28103.823306+1.371661%29&interval=10&api_key=yourapikey&email=youremail"
url_2017 = "https://developer.nrel.gov/api/nsrdb/v2/solar/himawari-download.csv?names=2017&wkt=POINT%28103.823306+1.371661%29&interval=10&api_key=yourapikey&email=youremail"
url_2018 = "https://developer.nrel.gov/api/nsrdb/v2/solar/himawari-download.csv?names=2018&wkt=POINT%28103.823306+1.371661%29&interval=10&api_key=yourapikey&email=youremail"
url_2019 = "https://developer.nrel.gov/api/nsrdb/v2/solar/himawari-download.csv?names=2019&wkt=POINT%28103.823306+1.371661%29&interval=10&api_key=yourapikey&email=youremail"
url_2020 = "https://developer.nrel.gov/api/nsrdb/v2/solar/himawari-download.csv?names=2020&wkt=POINT%28103.823306+1.371661%29&interval=10&api_key=yourapikey&email=youremail"

lst = ["2016","2017","2018","2019","2020"]

for year in lst:
    url = f"https://developer.nrel.gov/api/nsrdb/v2/solar/himawari-download.csv?names={year}&wkt=POINT%28103.823306+1.371661%29&interval=10&api_key={yourapikey}&email={youremail}"

    response = requests.get(url)
    with open(f'{year}.csv', 'wb') as opened_file:
        opened_file.write(response.content)
