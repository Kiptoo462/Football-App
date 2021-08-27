import os
import urllib.request,json
from .models import Source, Football 

api_key = None
football_url = None
sources_url = None

def configure_request(app):
  global api_key,sources_url,football_url
  api_key = app.config['FOOTBALL_API_KEY']
  football_url = app.config['FOOTBALL_API_BASE_URL']
  sources_url = app.config['SOURCES_API_BASE_URL']

source_path=''
  
def get_source_football(id):
    '''
    Function that gets the json response to our url  request
    '''
    get_football_url = sources_url.format(id,api_key)
    with urllib.request.urlopen(get_football_url) as url:
     
        get_football_data = url.read()
        get_football_response = json.loads(get_football_data)
        football_results = None
     
        if get_football_response['football']:
            football_results_list = get_football_response['football']
            football_results = process_results(football_results_list)
    return football_results
     
def process_results(football_list):
    '''
    Function  that processes the news result and transform them to a list of Objects
    Args:
        football_list: A list of dictionaries that contain football details
    Returns :
        football_results: A list of news objects
    '''
    football_results = []
    for football_item in football_list:
        id = football_item.get('id')
        author = football_item.get('author')
        title = football_item.get('title')
        description = football_item.get('description')
        url = football_item.get('url')
        datePublished = football_item.get('publishedAt')
        pathToImage = football_item.get('urlToImage')
            
        if pathToImage:
            football_object = Football(author,title,description,pathToImage,url,datePublished)
            football_results.append(football_object)
    return football_results    
      
def get_football_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = sources_url.format(category,api_key)
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)
        sources_results = None
        print(get_sources_response)
        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_sources_results(sources_results_list)
            
    return sources_results   
  
def process_sources_results(sources_list):
    '''
    Function  that processes the news result and transform them to a list of Objects
    Args:
        football_list: A list of dictionaries that contain news details
    Returns :
        football_results: A list of news objects
    '''
    sources_results = []
    for source in sources_list:
        id = source.get('id')
        name = source.get('name')
        description = source.get('description')
        url = source.get( 'url' )
        category = source.get('category')
            
        if id: 
            source_object = Source(id,name,description,url,category)
            sources_results.append(source_object)
    return sources_results  