from app.api import bp
import os
import requests
import json
from app.classes import Restaurant
from app.api.responses import success_response
api_key = os.getenv("API_KEY")
API_ENDPOINT = "https://api.yelp.com/v3/businesses/search"
@bp.route("restaurants", methods=["GET"])
def get_random_restaurant(location="irvine", limit=5):
    payload = {
        "location": location,
        "limit": 50,
        "categories":"japanese,chinese"
    }
    headers = {
        "Authorization" : "Bearer " + api_key
    }
    data = requests.get(API_ENDPOINT, params=payload, headers=headers)
    businesses = data.json()["businesses"]     
    businesses_objects = ingest_data(businesses)
    return success_response(200, payload=businesses_objects, message="Businesses loaded")


def ingest_data(data_json):
    # restaurant name, cuisine, image. hyperlink to the yelp page 
    restaurant_objects = []
    for i in data_json:
        restaurant_objects.append(Restaurant.Restaurant(i).return_object())
    return restaurant_objects

def construct_categories(categories):
    category_string = ""
    for i in categories:
        category_string += i + ','
    
    return category_string[:len(category_string)-1]
    