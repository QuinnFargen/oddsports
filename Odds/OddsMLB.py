
# import pymongo
import config
import requests
import json

from Storage.OddsMongo import mongo_insertone
from Odds.OddsAPI import oddsApi_get


sport = 'baseball_mlb'

mlb = oddsApi_get(sport)

mongo_insertone('Odds', 'MLB', mlb, loop=1)
