from app import flask_app as app
import json
from datetime import datetime
from flask import request


@app.route("/heartbeat")
def heartbeat():
    return json.dumps(
        {
            "status": True,
            "service": "Yige_Wang_Homework_1",
            "datetime": f"{datetime.now()}"
        }
    )


@app.route("/sum", methods= ['POST', 'GET'])
def sum():
    data = request.json
    x = data['x']
    y = data['y']

    return json.dumps(
        {
            "sum": x + y
        }
    )


@app.route("/minimum", methods= ['POST', 'GET'])
def minimum():
    data = request.json
    v = data['values']
    result = min(v)
    return json.dumps(
        {
            "minimum": result
        }
    )


@app.route("/product", methods= ['POST', 'GET'])
def product():
    data = request.json
    v = data['values']
    result = 1

    for i in v:
        result *= i

    if len(v) == 0:
        result = 0

    return json.dumps(
        {
            "product": result
        }
    )


@app.before_first_request
def load_app():
    print("Loading App Before First Request")
