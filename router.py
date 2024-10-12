from flask import Blueprint, jsonify


app_route = Blueprint('route', __name__)


@app_route.route('/hello')
def hello():
    return jsonify(answer = 'Hello world')