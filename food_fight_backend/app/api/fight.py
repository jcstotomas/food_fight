from app.api import bp
import os
import requests
import json
from app.api.responses import success_response
from flask import request, render_template


@bp.route("/fights", methods=["POST"])
def get_fight():
    restaurants = request.form["restaurant"]
    restaurant_split = restaurants.split(",")
    seen = set()
    for restaurant in restaurant_split:
        if restaurant.lower() not in seen:
            seen.add(restaurant.lower())
    pairs = []
    seen_list = list(seen)
    if len(seen_list) > 1:
        for i in range(0,len(seen_list), 2):
            first_restaurant = seen_list[i]
            if (i+1 == len(seen_list)):
                second_restaurant = None
            else:
                second_restaurant = seen_list[i+1]
            pairs.append([first_restaurant, second_restaurant, "pair" + str(i)])

    return render_template('fight_results.html', pairs = pairs)