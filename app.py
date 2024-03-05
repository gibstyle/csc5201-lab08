from flask import Flask, request, jsonify
from service import RestaurantService
from models import Schema

import json

app = Flask(__name__)


@app.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = "*"
    response.headers['Access-Control-Allow-Headers'] =  "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
    response.headers['Access-Control-Allow-Methods']=  "POST, GET, PUT, DELETE, OPTIONS"
    return response

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/<name>")
def hello_name(name):
    return "Hello " + name


@app.route("/restaurant", methods=["GET"])
def list_restaurants():
    return jsonify(RestaurantService().list())


@app.route("/restaurant", methods=["POST"])
def create_restaurant():
    return jsonify(RestaurantService().create(request.get_json()))


@app.route("/restaurant/<restaurant_id>", methods=["PUT"])
def update_restaurant(restaurant_id):
    return jsonify(RestaurantService().update(restaurant_id, request.get_json()))


@app.route("/restaurant/<restaurant_id>", methods=["GET"])
def get_restaurant(restaurant_id):
    return jsonify(RestaurantService().get_by_id(restaurant_id))


@app.route("/restaurant/<restaurant_id>", methods=["DELETE"])
def delete_restaurant(restaurant_id):
    return jsonify(RestaurantService().delete(restaurant_id))


if __name__ == "__main__":
    Schema()
    app.run(debug=True, host='127.0.0.1', port=8888)