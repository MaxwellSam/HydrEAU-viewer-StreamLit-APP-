"""
File: toolbox.py
Description: contain tool's methods
Author: Sam Maxwell
Date: 02/2022
"""

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
    """
    Description: Parse the end of the API request to extract information
    Input: 
        request: 
            type: str
            desc: constain request information spaced by special characters
    output: 
        infos_request: 
            type: dic
            decs: keys are kind of filter parameters (expl: by localisation or region) and there values as list of strings. 
    """
    infos_request = {}
    filter = {}
    splited_request = request.split('?')
    infos_request["domain"]=splited_request[0]
    for i in splited_request[1].split('&'):
        i = i.split('=')
        infos_request[i[0]]=i[1].split(',')
    return infos_request

## for 
def localisation_request_to_url(infos_request):
    url_hubEAU = var.url_hydro_stations
    for key in infos_request.keys():
        if key == "domaine": pass
        else:
            url_hubEAU+="&%s%s"%(key,infos_request[key])
    return url_hubEAU 
    # url_hubEAU += "&longitude=%s" % (infos_request["longitude"])
    # url_hubEAU += "&latitude=%s" % (infos_request["latitude"])




def region_request_to_url(infos_request):
    url_hubEAU = var.url_hydro_stations
    for key in infos_request.keys():
        if key == "domaine": pass
        else:
            url_hubEAU+="&%s%s"%(key, ','.join(infos_request[key]))
    return url_hubEAU

def stations_request_to_url(request):
    infos_request = parser_request(request)
    if infos_request["domain"] == "localisation":
        return localisation_request_to_url(infos_request)
    elif infos_request["domain"] == "region":
        return region_request_to_url(infos_request)
