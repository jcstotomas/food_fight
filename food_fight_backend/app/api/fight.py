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

    
    return "Asdf"