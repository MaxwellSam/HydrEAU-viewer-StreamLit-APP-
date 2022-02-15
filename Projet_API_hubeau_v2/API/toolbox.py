"""
File: toolbox.py
Description: contain tool's methods
Author: Sam Maxwell
Date: 02/2022
"""

from flask import abort
import requests
import pandas as pd 
import json

import variables as var

def url_hubeau_to_json(url):
    response = requests.get(url, verify=False)
    return json.loads(response.text)


"""
----------------------------------------------------------
                Creating Request for hubEAU
----------------------------------------------------------
"""

# parser request API: 

def parser_request(request):
    infos_request = {}
    filter = {}
    splited_request = request.split('>>') # note: does not work with '?'
    infos_request["type"]=splited_request[0]
    infos_request["request_content"] = {}
    for i in splited_request[1].split('&'):
        i = i.split('=')
        infos_request["request_content"][i[0]]=i[1].split(',')
    return infos_request

## for stations data 

def hydro_station_request_coord_to_url(request_content):
    # return {"it s ok":request_content}
    request_hubeau = var.url_hydro_stations_filtre+"&longitude=%s&latitude=%s&distance=%s"%(request_content["longitude"][0], request_content["latitude"][0], request_content["distance"][0])
    return url_hubeau_to_json(request_hubeau)

def hydro_station_request_to_url(request):
    request_parsed = parser_request(request)
    if request_parsed["type"] == "coord":
        return hydro_station_request_coord_to_url(request_parsed["request_content"])
    else: 
        abort(400)
