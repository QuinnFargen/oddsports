
# import pymongo
import config
import requests
import json

from Storage.OddsMongo import mongo_insertone
from Odds.OddsAPI import oddsApi_get


sport = 'basketball_nba'

nba = oddsApi_get(sport)

mongo_insertone('Odds', 'NBA', nba, loop=1)

