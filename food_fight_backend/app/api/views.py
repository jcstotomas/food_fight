from app.api import bp
import os
import requests
import json
from app.api.responses import success_response
from flask import render_template, request

@bp.route("/", methods=["GET"])
@bp.route("home", methods=["GET"])
def get_home():
    return render_template('Home.html')

@bp.route("random", methods=["GET"])
def get_random():
    # data = request.form["location"]
    return render_template('random_restaurant.html')


@bp.route("fight", methods=["GET"])
def fight():
    return render_template('fight.html')