from app.api import bp
import os
import requests
import json
from app.api.responses import success_response
from flask import render_template

@bp.route("home", methods=["GET"])
def get_home():
    return render_template('Home.html')

@bp.route("random", methods=["GET"])
def get_random():
    return render_template('random_restaurant.html')