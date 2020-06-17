from app.api import bp
import os
import requests
from app.classes import Restaurant
api_key = os.getenv("API_KEY")
API_ENDPOINT = "https://api.yelp.com/v3/businesses/search"
@bp.route("restaurants", methods=["GET"])
def get_random_restaurant(location="irvine", limit=5):
    payload = {
        "location": location,
        "limit": 5
    }
    headers = {
        "Authorization" : "Bearer " + api_key
    }
    data = requests.get(API_ENDPOINT, params=payload, headers=headers)
    return data.json()



def ingest_data(data_json):
    # restaurant name, cuisine, image. hyperlink to the yelp page 
    
    pass