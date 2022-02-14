"""
File: API.py
Description: API for requesting hubeau
Author: Sam Maxwell
Date: 02/2022
"""

from flask import Flask, escape, request, template_rendered
import pandas as pd
import toolbox as tb
import variables as var

API = Flask(__name__)

# Routes
@API.route("/")
def origin():
    return {"origine":"API Project with hubEAU"}
## rivers temperature
@API.route("/river_temp")
def river_temp():
    return "TODO"
### stations
@API.route("/river_temp/station")
def river_temp_station():
    return tb.url_hubeau_to_json(var.url_river_temp_station)

# @API.route("/river_temp/<string:request>")
# def river_temp_request(request): 
#     """
#     Description: parse the request to generate the appropriate request for hubeau and return the response.
#     input: 
#         request: a string which containe request's informations (expl: specific region, recording time start, etc.)
#     output:
#         json from hubeau according to the request   
#     """
#     url_request = parser_request(request)

# @API.route("/river_temp/station/<string:request>")
#     url_request = parser_request_station(request)

@API.route("/hydro/stations")
def hydro_stations():
    return tb.url_hubeau_to_json(var.url_hydro_stations)

## 

# Run API

if __name__ == "__main__":
    API.run(debug=True)
