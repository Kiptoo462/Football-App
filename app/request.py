import urllib.request,json,http.client
from .models import User
from datetime import datetime
import requests

today = datetime.today().strftime('%Y-%m-%d')

api_key = '306537220f31131e7ffaa395a0a1f6869677028939925eaa1c8eb7532dfddcc8'
base_url = 'https://apiv3.apifootball.com/?action=get_countries&APIkey={}'

def configure_request(app):
    global api_key,base_url
    api_key = '306537220f31131e7ffaa395a0a1f6869677028939925eaa1c8eb7532dfddcc8'
    base_url = 'https://apiv3.apifootball.com/?action=get_countries&APIkey={}'


def getTestCall():
    response = requests.get('https://api.football-data-api.com/test-call?key=test85g57')
    if response.status_code == 200:
        print(response.json())
        return response.json()


def getLeagues():
    response = requests.get('https://api.football-data-api.com/league-list?key=test85g57')
    if response.status_code == 200:
        print(response.json())
        return response.json()

    
def getCountries():
    response = requests.get('https://api.football-data-api.com/country-list?key=test85g57')
    if response.status_code == 200:
        print(response.json())
        return response.json()


def getPlayer():
    response = requests.get('https://api.football-data-api.com/player?key=test85g57&player_id={}')
    if response.status_code == 200:
        print(response.json())
        return response.json()


def getTeam():
    response = requests.get('https://api.football-data-api.com/team?key=test85g57&team_id={}')
    if response.status_code == 200:
        print(response.json())
        return response.json()


def getEPLProfile():
    response = requests.get('https://api.football-data-api.com/league-season?key=test85g57&id=161&season_id=2021')
    if response.status_code == 200:
        print(response.json())
        return response.json()