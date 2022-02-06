from flask import Flask, jsonify
import pandas as pd
import json
import data

apply = Flask(__name__)

@apply.route("/")
def all_data():
    # result = data.df.to_json(orient="columns")
    # result = data.df.to_json(orient="split")
    result = data.df.to_json(orient="index")
    # js = data.df.to_json(orient="records")
    js = data.df.to_json(orient="split")
    # return json.loads(json.dumps(js))
    # return jsonify(json.loads(js))
    # return json.loads(js)
    # return json.loads(result)
    return json.loads(result)

@apply.route("/groupby")
def groupby():
    return json.loads(data.df_groupby.to_json())

@apply.route("/index")
def index():
    return json.loads(data.df_index.to_json(orient="index"))

@apply.route("/REGION/<string:region_name>")
def region(region_name):
    if (region_name not in data.df["region"]):
        return "region not in dataframe"
    else:
        df_region = data.filter_region(region_name, data.df)
        result = df_region.to_json(orient="split")
        return json.loads(result)


if __name__ == "__main__":
    apply.run(debug=True)
