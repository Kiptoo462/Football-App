import urllib.request,json,http.client
from .models import User,Country
from datetime import datetime
import requests

today = datetime.today().strftime('%Y-%m-%d')

api_key = '306537220f31131e7ffaa395a0a1f6869677028939925eaa1c8eb7532dfddcc8'
base_url = 'https://apiv3.apifootball.com/?action=get_countries&APIkey={}'

def configure_request(app):
    global api_key,base_url
    api_key = '306537220f31131e7ffaa395a0a1f6869677028939925eaa1c8eb7532dfddcc8'
    base_url = 'https://apiv3.apifootball.com/?action=get_countries&APIkey={}'


def getTeam():
    response = requests.get('https://apiv3.apifootball.com/?action=get_teams&team_id=73&APIkey=306537220f31131e7ffaa395a0a1f6869677028939925eaa1c8eb7532dfddcc8')
    if response.status_code == 200:
        print(response.json())
        return response.json()