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
    tmp = json.loads(tmp)
    return pd.DataFrame.from_dict(tmp, orient='index')
    # return pd.read_json(tmp, orient ='index')

# def load_data_stations(long, lat, dist):
#     if long == 0 or lat == 0 or dist == 0:
#         return generate_dataframe(var.url_hydro_stations)
#     else:
#         return generate_dataframe(var.generate_url_coord(long, lat, dist))


#####################################################################################################
#                                        HYDRO OBS                                                  #
#####################################################################################################

def load_data_hydro_obs_elab(long, lat, dist, days_before):
    df_stations = load_data_stations(long, lat, dist)
    stations = df_stations.code_station.tolist()
    url = var.generate_url_hydro_obs_elab(stations, days_before)
    # tmp = fetch_data(var.generate_url_hydro_obs(stations, days_before))
    tmp = fetch_data(url)
    # return pd.read_json(tmp, orient="index")
    tmp = json.loads(tmp)
    return pd.DataFrame.from_dict(tmp, orient='index')

def load_data_hydro_obs_tr(long, lat, dist, days_before):
    df_stations = load_data_stations(long, lat, dist)
    stations = df_stations.code_station.tolist()
    url = var.generate_url_hydro_obs_tr(stations, days_before)
    tmp = fetch_data(url)
    tmp = json.loads(tmp)
    # return tmp
    df = pd.DataFrame.from_dict(tmp, orient='index')
    return df
    # df = pd.read_json(tmp, orient="index")
    # return df 
    df_Q = df[df["grandeur_hydro"] == "Q"].loc[:, df.columns!="grandeur_hydro"]
    df_Q = df_Q.rename(columns={'resultat_obs':'Q'}, inplace=True)

    df_H = df[df["grandeur_hydro"] == "H"].loc[:, df.columns!="grandeur_hydro"]
    df_H = df_H.rename(columns={'resultat_obs':'H'}, inplace=True)
    # df_Q = df[df["grandeur_hydro"] == "H"].rename(columns={"resultat_obs":"H"}).pop("grandeur_hydro")
    return pd.merge(df_H, df_Q)

