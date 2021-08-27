import urllib.request,json,http.client
from .models import User, Team, League, Player
from datetime import datetime
import requests
import http.client
import json

today = datetime.today().strftime('%Y-%m-%d')


def configure_request(app):
    global api_key,base_url
    api_key = 'test85g57'
    base_url = 'https://api.football-data-api.com/?key={}'


def getTestCall():
    response = requests.get('https://api.football-data-api.com/test-call?key=test85g57')
    if response.status_code == 200:
        print(response.json())
        return response.json()


def getLeagues():
    response = requests.get('https://app.sportdataapi.com/api/v1/soccer/leagues?apikey=01437170-06ed-11ec-8721-6bf19042e66d')
    if response.status_code == 200:
        print(response.json())
        return response.json()


# def getPlayer():
#     response = requests.get('')
#     if response.status_code == 200:
#         print(response.json())
#         return response.json()


# def getTeam():
#     response = requests.get('')
#     if response.status_code == 200:
#         print(response.json())
#         return response.json()