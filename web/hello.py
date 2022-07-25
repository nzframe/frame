from flask import Flask, jsonify, request
from flask_cors import CORS
import json
app = Flask(__name__)
CORS(app)


@app.route("/test")
def hello_world():
    with open("./data/E1.txt") as fd:
        lines = fd.read().splitlines()

    response = jsonify({"data": lines})
    return response


@app.route("/json", methods=["POST"])
def hello_json():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        return json
    else:
        return 'Content-Type not supported!'

@app.route("/wall", methods=["POST"])
def hello_wall():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        rt = request.json
        aDict = json.loads(rt)
        return aDict[0]["type"]
    else:
        return 'Content-Type not supported!'