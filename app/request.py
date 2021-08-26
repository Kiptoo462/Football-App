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
    base_url = 'https://apiv3.apifootball.com/?action=get_countries&APIkey={}'


def get_competition():
    url = "https://apiv3.apifootball.com/?action=get_countries&APIkey=306537220f31131e7ffaa395a0a1f6869677028939925eaa1c8eb7532dfddcc8"
    response = requests.request("GET", url)
    
    print(response.text)

    with urllib.request.urlopen(url) as url:
        competition_details_data = url.read()
        competition_details_response = json.loads(competition_details_data)

        competition_object = None
        if competition_details_response:
            id = competition_details_response.get('id')
            name = competition_details_response.get('name')
            plan = competition_details_response.get('plan')

            competition_object = Competition(id,name,plan)

    return competition_object