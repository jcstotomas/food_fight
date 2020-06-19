from flask import Blueprint

bp = Blueprint('api', __name__)


@bp.route('/', methods=['GET'])
def get_status():
    return {"status": "api is running"}

from app.api import restaurant, views