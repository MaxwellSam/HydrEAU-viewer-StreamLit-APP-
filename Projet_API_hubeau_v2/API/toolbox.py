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
from datetime import date, timedelta

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


def hydro_station_coord_to_url(args):
    """
    Description: get the arguments of request and generate the url for requesting hubEAU API
    input: 
        args: 
            type: dict <str, str>
            desc: contain request's arguments
    output : 
        url_hubeau: 
            type: str
            desc: the url created for requesting hubeau API 
    """
    url_hubeau = var.url_hydro_stations_filtre
    for k in args.keys():
        if k not in var.translate_key_word.keys():
            abort(400)
        url_hubeau += "&%s=%s"%(var.translate_key_word[k], args[k])
    return url_hubeau

## for hydro observations 

def find_date_to_start(type, nbr):
    """
    Description: Return the date before the curent date according to the type (D for days, M for months and Y for years) and the number (nbr)
    input:
        type: 
            type: str
            desc: interval of time 
        nbr:
            type: str
            desc: number of intervals
    output:
        day_to_start:
            type:str
            desc: day which begin the data history
    """
    today = date.today()
    # str_date = today.strftime("%Y-%m-%d")
    # n_days_ago = today - timedelta(days=5)
    # print(today, n_days_ago) 
    if type == "D":
        day_to_start = today - timedelta(days=int(nbr))
        return day_to_start
    if type == "M":
        day_to_start = today - timedelta(days=int(nbr)*30)
        return day_to_start
    if type == "Y":
        day_to_start = today - timedelta(days=int(nbr)*365)
        return day_to_start
    else:
        abort(400)
        
def hydro_obs_to_url(args):
    # url_hubeau = var.url_hydro_obs+"?"
    url_hubeau = var.url_hydro_obs_filtred
    for k in args.keys():
        if k in var.translate_timedate.keys():
            # find date to start for x days of data (expl: J=5)
            date_to_start = find_date_to_start(k, args[k])
            # url_hubeau += "%s=%s&"%(var.translate_timedate[k], date_to_start)
            url_hubeau += "&%s=%s"%(var.translate_timedate[k], date_to_start)
        elif k not in var.translate_key_word.keys():
            abort(400)
        else:
            # url_hubeau += "%s=%s&"%(var.translate_key_word[k], args[k])
            url_hubeau += "&%s=%s"%(var.translate_key_word[k], args[k])
    # return url_hubeau[:-1] # delete '&' end of str
    return url_hubeau 

