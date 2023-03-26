
import pymongo
import config
import requests
import json



sport = 'basketball_nba'
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
# len(result_list)
# result_list[0]
# response.json()

################
# MongoDB

myclient = pymongo.MongoClient(config.mango)
mydb = myclient["Sports"]
mycol = mydb["NBA"]

for r in range(len(result_list)):
    x = mycol.insert_one(result_list[r])