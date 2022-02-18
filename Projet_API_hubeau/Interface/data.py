"""
File: data.py
Description: contain methods to construct dataset
Author: Sam Maxwell
Date: 02/2022
"""

import streamlit as st
import variables as var
import pandas as pd
import json 
import requests

#####################################################################################################
#                                        STATIONS                                                   #
#####################################################################################################

@st.cache
def fetch_data(url):
    resp = requests.get(url)
    return resp.text
    # data_json = json.loads(resp.text)
    # return pd.DataFrame(data_json["data"])
    # return pd.DataFrame.from_dict(data_json)

def load_data_stations(long, lat, dist):
    if long == 0 or lat == 0 or dist == 0:
        tmp = fetch_data(var.url_hydro_stations)
    else:
        tmp = fetch_data(var.generate_url_coord(long, lat, dist))
    # data_json = json.loads(tmp)
    # return pd.DataFrame(data_json["data"])
    # return pd.DataFrame(data_json)
    return pd.read_json(tmp, orient ='index')

# def load_data_stations(long, lat, dist):
#     if long == 0 or lat == 0 or dist == 0:
#         return generate_dataframe(var.url_hydro_stations)
#     else:
#         return generate_dataframe(var.generate_url_coord(long, lat, dist))


#####################################################################################################
#                                        HYDRO OBS                                                  #
#####################################################################################################

def load_data_hydro_obs(long, lat, dist, days_before):
    df_stations = load_data_stations(long, lat, dist)
    stations = df_stations.code_station.tolist()
    url = var.generate_url_hydro_obs(stations, days_before)
    tmp = fetch_data(var.generate_url_hydro_obs(stations, days_before))
    return pd.read_json(tmp, orient="index")

