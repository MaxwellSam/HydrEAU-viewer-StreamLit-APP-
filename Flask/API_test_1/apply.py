from flask import Flask
import pandas as pd
import json
import data

apply = Flask(__name__)

@apply.route("/")
def all_data():
    js = data.df.to_json(orient="records")
    # return json.loads(json.data.df)
    return "ok"

apply.run()