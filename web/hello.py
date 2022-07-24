from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/test")
def hello_world():
    with open("./data/E1.txt") as fd:
        lines = fd.read().splitlines()

    response = jsonify({"data": lines})
    response.headers.add("Access-Control-Allow-Origin", "http://localhost:3000")
    return response
