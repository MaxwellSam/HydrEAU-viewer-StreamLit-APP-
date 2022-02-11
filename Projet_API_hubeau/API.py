"""
File: API.py
Description: API for requesting hubeau
Author: Sam Maxwell
Date: 02/2022
"""

from flask import Flask, escape, request
import pandas as pd
import toolbox as tb
import variables as var

API = Flask(__name__)

# Routes
@API.route("/")
def origin():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'
## rivers temperature
@API.route("/river_temp")
def river_temp():
    return "TODO"
### stations
@API.route("/river_temp/station")
def river_temp_station():
    return tb.url_hubeau_to_json(var.url_river_temp_station)

@API.

## 

# Run API

if __name__ == "__main__":
    API.run(debug=True)
