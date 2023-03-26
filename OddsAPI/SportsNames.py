import pymongo
import config
import requests
import json

###############
# Odds API

url = "https://api.apilayer.com/odds/sports?all=false"

payload = {}
headers= {"apikey": config.odds_API_key}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text
# print(result)
result_list = json.loads(result)

################
# MongoDB

myclient = pymongo.MongoClient(config.mango)
mydb = myclient["Sports"]
mycol = mydb["Names"]

for r in range(len(result_list)):
    x = mycol.insert_one(result_list[r])



