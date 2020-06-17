
from flask import jsonify 
from werkzeug.http import HTTP_STATUS_CODES

def success_response(status_code, payload=None, message= None):
    obj = {"status": HTTP_STATUS_CODES.get(status_code, "success")}
    if message:
        obj['message'] = message
        obj["code"] = status_code
    if payload:
        obj["data"] = payload

    response = jsonify(obj)
    response.status_code = status_code
    return response
