
# import pymongo
import config
import requests
import json

from Storage.OddsMongo import mongo_insertone


sport = 'baseball_mlb'
regions = 'us'
oddsFormat = 'decimal'
markets = 'h2h,spreads,totals'
dateFormat = 'iso'
url = "https://api.apilayer.com/odds/sports/"+sport+"/odds?regions="+regions+"&oddsFormat="+oddsFormat+"&markets="+markets+"&dateFormat="+dateFormat+""

payload = {}
headers= {  "apikey": config.odds_API_key}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
# result = response.text
# print(result)
result_list = json.loads(response.text)
len(result_list)
# result_list[0]
# response.json()

################
# MongoDB


mongo_insertone('Stats', 'MLB', result_list, loop=1)

# myclient = pymongo.MongoClient(config.mango)
# mydb = myclient["Odds"]
# mycol = mydb["MLB"]

# for r in range(len(result_list)):
#     x = mycol.insert_one(result_list[r])