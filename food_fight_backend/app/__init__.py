from flask import Flask
import os
from app.api import bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp, url_prefix="/")
    return app
