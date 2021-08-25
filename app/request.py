import urllib.request,json,http.client
from .models import User, Competition
from datetime import datetime
import requests

today = datetime.today().strftime('%Y-%m-%d')

api_key = '060161c1c7814b35b3f438c8580388a2'
base_url = 'http://api.football-data.org/v2/competitions/'

def configure_request(app):
    global api_key,base_url
    api_key = '060161c1c7814b35b3f438c8580388a2'
    base_url = 'http://api.football-data.org/v2/competitions/'


def get_competition():
    url = "http://api.football-data.org/v2/competitions/"
    response = requests.request("GET", url)
    
    print(response.text)