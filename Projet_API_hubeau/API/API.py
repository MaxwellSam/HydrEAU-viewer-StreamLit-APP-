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
import json

API = Flask(__name__)

# Routes
@API.route("/")
def origin():
    return {"origine":"API Project with hubEAU"}

## Hydro data 

### Stations
 
@API.route("/hydro/stations")
def hydro_stations():
    return tb.url_hubeau_to_json(var.url_hydro_stations_filtre)

@API.route("/hydro/stations/coord")
def hydro_stations_coord():
    """
    Description: Return all active stations at the specified distance of the given coordinate
    Exemple : coord?long=-0.57918&lat=44.837789&dist=30 (Bordeaux coordinate)
    args: 
        long: longitude
        lat: latitude
        dist: distance
    output:
        type: json
        desc: hydro stations at 30 km of the specified coordinate
    """
    url = tb.hydro_station_coord_to_url(request.args)
    return tb.url_hubeau_to_json(url)
    
### data hydro

@API.route("/hydro/obs_elab")
def hydro_obs_elab():
    """
    Description: Return hydro observation elaborate (daily average flow 'QmJ' or monthly average flow 'QmM') for the stations listed
    Exemple: /hydro/obs_elab?hydro_type=QmJ&stations=O965000101,O972001001&date_start_obs=2022-02-15
             /hydro/obs_elab?hydro_type=QmJ&stations=O965000101,O972001001&D=5
    args:
        hydro_mesure_elab: the type of hydro obs ('QmJ' or 'QmM')
        station: stations selected (spaced by a comma)
        day_start_obs: the day at start the observation
        J: number of day before curent date
    output:
        type: json
        desc: the hydro observations since the day specified for the stations wished  
    """
    if bool(request.args) == False:
        return tb.url_hubeau_to_json(var.url_hydro_obs_elab_filtred)
    url = tb.hydro_obs_to_url("obs_elab",request.args)
    # file = tb.url_hubeau_to_json(url)
    # data = file["data"]
    # return  {i:data[i] for i in range(len(data))}
    # return url
    return tb.url_hubeau_to_json(url)


@API.route("/hydro/obs_tr")
def hydro_obs_tr():
    """
        Description: Return hydro observation "real time" (water tide 'H' and flow 'Q') for the stations listed
        Exemple: /hydro/obs_tr?stations=O965000101,O972001001&date_start_obs=2022-02-15
                /hydro/obs_tr?stations=O965000101,O972001001&D=5
        args:
            hydro_mesure_tr: the type of hydro mesure ('H' or 'Q')
            station: stations selected (spaced by a comma)
            day_start_obs: the day at start the observation
            J: number of day before curent date
        output:
            type: json
            desc: the hydro observations "real time" since the day specified for the stations wished  
    """ 
    if bool(request.args) == False:
        return tb.url_hubeau_to_json(var.url_hydro_obs_tr_filtred)
    # return str(request)+ " - "+str(request.args)
    url=tb.hydro_obs_to_url("obs_tr",request.args)
    # return url
    return tb.url_hubeau_to_json(url)


# Run API

if __name__ == "__main__":
    API.run(debug=True)
