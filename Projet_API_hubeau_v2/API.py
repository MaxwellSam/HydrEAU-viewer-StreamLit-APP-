"""
File: API.py
Description: API for requesting hubEAU
Author: Sam Maxwell
Date: 02/2022
"""

from cmath import inf
from flask import Flask, escape, request, template_rendered
import pandas as pd
import toolbox as tb
import variables as var

API = Flask(__name__)

# Routes
@API.route("/")
def origin():
    return {"origine":"API Project with hubEAU"}

## Hydro data 

### Stations
 
@API.route("/hydro/stations")
def hydro_stations():
    return tb.url_hubeau_to_json(var.url_hydro_stations)

@API.route("/hydro/<string:request>")
def hydro_stations_request(request):
    hydro_request_to_url(request)
    return 
    
## 

# Run API

if __name__ == "__main__":
    API.run(debug=True)
