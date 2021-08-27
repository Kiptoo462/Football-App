import urllib.request,json,http.client
from .models import User, Team, Player
from datetime import datetime
import requests
import http.client
import json

today = datetime.today().strftime('%Y-%m-%d')


def configure_request(app):
    global api_key,base_url
    api_key = 'test85g57'
    player_url = 'https://api.football-data-api.com/?key={}'
    team_url = 'https://api.football-data-api.com/?key={}'


def getTestCall():
    response = requests.get('https://api.football-data-api.com/test-call?key=test85g57')
    if response.status_code == 200:
        print(response.json())
        return response.json()


# def getPlayer(id):
#     getPlayer = player_url.format(id)
#     print(getPlayer)

#     with requests.get(getPlayer) as data:
#         getPlayer_data = data.json()
#         getPlayer_response = getPlayer_data

#     return getPlayer_response