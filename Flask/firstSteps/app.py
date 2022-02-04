from logging import exception
# from flask import Flask, render_template
from flask import *
import pandas as pd
import json
import localData

myString = "this is a string"

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/data")
def data():
    l = []
    l.append(1)
    l.append(2)
    return {"list":l}

@app.route("/txt")
def txt():
    data()
    return localData.dataTXT

@app.route("/dataframe")
def dataframe():
    return render_template('view.html', tables=[localData.dataCSV.to_html(classes='data')], titles=localData.dataCSV.columns.values)
# methods
# myString = "this is a string"
# txt(myString)

@app.route("/API/ALLDATA")
def all_data():
    js = localData.df_meteo.to_json(orient="records")
    js = json.dumps(js)
    print(js)
    return json.loads(js)

app.run()
    
