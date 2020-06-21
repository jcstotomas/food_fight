from app.api import bp
import os
import requests
import json
from app.classes import Restaurant
from app.api.responses import success_response
from flask import request, render_template
from random import randint
api_key = os.getenv("API_KEY")
API_ENDPOINT = "https://api.yelp.com/v3/businesses/search"
@bp.route("restaurants", methods=["POST"])
def get_random_restaurant():
    payload = {
        "location": request.form["location"],
        "limit": 50,
        "categories": construct_categories(request.form.getlist("cuisine"))
    }
    headers = {
        "Authorization" : "Bearer " + api_key
    }
    results_limit = int(request.form["limit"])
    data = requests.get(API_ENDPOINT, params=payload, headers=headers)
    businesses = data.json()["businesses"]     
    businesses_objects = ingest_data(businesses)
    print(payload["categories"])
    filtered_businesses = randomize_business(businesses_objects, results_limit)
    return render_template("random_result.html", results=filtered_businesses)




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
    

def randomize_business(businesses, result_limit):
    numbers_seen = set()
    filtered_businesses = []
    while len(numbers_seen) != result_limit:
        num = randint(0,len(businesses)-1)
        if num not in numbers_seen:
            numbers_seen.add(num)
            filtered_businesses.append(businesses[num])
    return filtered_businesses
