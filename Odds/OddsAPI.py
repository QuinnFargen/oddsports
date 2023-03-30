
import requests
import json
import config


def oddsApi_get(sport):
    # sport = 'basketball_nba' # baseball_mlb
    regions = 'us'
    oddsFormat = 'decimal'
    markets = 'h2h,spreads,totals'
    dateFormat = 'iso'
    url = "https://api.apilayer.com/odds/sports/"+sport+"/odds?regions="+regions+"&oddsFormat="+oddsFormat+"&markets="+markets+"&dateFormat="+dateFormat+""

    payload = {}
    headers= {  "apikey": config.odds_API_key}

    response = requests.request("GET", url, headers=headers, data = payload)
    status_code = response.status_code
    result_list = json.loads(response.text)
    return result_list