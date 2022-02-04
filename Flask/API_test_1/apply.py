from flask import Flask
import pandas as pd
import json
import data

apply = Flask(__name__)

@apply.route("/")
def all_data():
    # js = data.df.to_json(orient="records")
    js = data.df.to_json(orient="split")
    # return json.loads(json.dumps(js))
    # return jsonify(json.loads(js))
    return json.loads(js)

