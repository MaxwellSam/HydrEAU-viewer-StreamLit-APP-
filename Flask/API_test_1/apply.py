from flask import Flask, jsonify
import pandas as pd
import json
import data

apply = Flask(__name__)

@apply.route("/")
def all_data():
    result = data.df.to_json(orient="index")
    return json.loads(result)

@apply.route("/groupby")
def groupby():
    """
    return dataframe grouped by as json
    """
    return json.loads(data.df_groupby.to_json())

@apply.route("/index")
def index():
    """
    return dataframe indexed as json 
    """
    return json.loads(data.df_index.to_json(orient="index"))

@apply.route("/REGION/<string:region_name>")
def region(region_name):
    """
    return dataframe of `region_name` as json
    """
    if (region_name not in data.df.values):
        return {'message':'bad request, '+region_name+' not in df'}, 400
    else :
        df_region = data.filter_region(region_name, data.df)
        result = df_region.to_json(orient="index")
        return json.loads(result)


if __name__ == "__main__":
    apply.run(debug=True)
