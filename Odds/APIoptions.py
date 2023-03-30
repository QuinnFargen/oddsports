import pymongo
import config
import requests
import json

###############
# Odds API

url = "https://api.apilayer.com/odds/sports?all=true"

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
mydb = myclient["Odds"]
mycol = mydb["APIoptions"]

for r in range(len(result_list)):
    x = mycol.insert_one(result_list[r])



###################################

import statsapi

teams = statsapi.get(endpoint='teams',params={'sportId': 1})
teams


import pymongo
import config
import requests
import json

myclient = pymongo.MongoClient(config.mango)
mydb = myclient["Stats"]
mycol = mydb["MLB"]

mycol.insert_one(teams)


from Storage.OddsMongo import mongo_insertone

mongo_insertone('Stats', 'MLB', teams)
teams



sched = statsapi.schedule(start_date='07/01/2023',end_date='07/31/2023')

sched[0]



##########################



from nba_api.stats.endpoints import playercareerstats

# Nikola Jokić
career = playercareerstats.PlayerCareerStats(player_id='203999') 

# pandas data frames (optional: pip install pandas)
career.get_data_frames()[0]

# json
career.get_json()

# dictionary
career.get_dict()


from nba_api.stats.endpoints import leaguegamelog


leaguegl = leaguegamelog.LeagueGameLog(date_from_nullable='2023-03-20') 
l = leaguegl.get_dict()
leaguegl.get_json()

list(l)[1]