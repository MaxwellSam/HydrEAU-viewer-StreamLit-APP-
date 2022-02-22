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
    json_data = json.loads(tmp)
    df = pd.DataFrame.from_dict(json_data, orient='index')
    df = df.rename(columns={"date_obs_elab":"date_obs", "resultat_obs_elab":"QmJ"})
    return df
# def load_data_hydro_obs_tr(long, lat, dist, days_before):
#     df_stations = load_data_stations(long, lat, dist)
#     stations = df_stations.code_station.tolist()
#     url = var.generate_url_hydro_obs_tr(stations, days_before)
#     tmp = fetch_data(url)
#     tmp = json.loads(tmp)
#     # return tmp
#     df = pd.DataFrame.from_dict(tmp, orient='index')
#     # return df
#     # df = pd.read_json(tmp, orient="index")
#     # return df 
#     df_Q = df[df["grandeur_hydro"] == "Q"].loc[:, df.columns!="grandeur_hydro"]
#     df_Q = df_Q.rename(columns={'resultat_obs':'Q'}, inplace=True)

#     df_H = df[df["grandeur_hydro"] == "H"].loc[:, df.columns!="grandeur_hydro"]
#     df_H = df_H.rename(columns={'resultat_obs':'H'}, inplace=True)
#     # df_Q = df[df["grandeur_hydro"] == "H"].rename(columns={"resultat_obs":"H"}).pop("grandeur_hydro")
#     return pd.merge(df_H, df_Q)

def creat_df_tr_from_url(url, hydro_mesure):
    tmp = fetch_data(url)
    json_data = json.loads(tmp)
    df = pd.DataFrame.from_dict(json_data, orient="index")
    if hydro_mesure == 'H':
        df = df.rename(columns={'resultat_obs':'H'})
        df = df.loc[:, df.columns!="grandeur_hydro"]
    elif hydro_mesure == 'Q':
        df = df.rename(columns={'resultat_obs':'Q'})
        df = df.loc[:, df.columns!="grandeur_hydro"]
    return df


def load_data_hydro_obs_tr(long, lat, dist, days_before):
    ## stations ##
    df_stations = load_data_stations(long, lat, dist)
    stations = df_stations.code_station.tolist()
    ## data hydro tr ##
    url_H = var.generate_url_hydro_obs_tr_H(stations, days_before)
    url_Q = var.generate_url_hydro_obs_tr_Q(stations, days_before)
    df_H = creat_df_tr_from_url(url_H, 'H')
    df_Q = creat_df_tr_from_url(url_Q, 'Q')
    return pd.merge(df_H, df_Q, how='outer')

def load_data_hydro_obs_tr_H(long, lat, dist, days_before):
    ## stations ##
    df_stations = load_data_stations(long, lat, dist)
    stations = df_stations.code_station.tolist()
    ## data hydro tr ##
    url_H = var.generate_url_hydro_obs_tr_H(stations, days_before)
    return creat_df_tr_from_url(url_H, 'H')

def load_data_hydro_obs_tr_Q(long, lat, dist, days_before):
    ## stations ##
    df_stations = load_data_stations(long, lat, dist)
    stations = df_stations.code_station.tolist()
    ## data hydro tr ##
    url_Q = var.generate_url_hydro_obs_tr_Q(stations, days_before)
    return creat_df_tr_from_url(url_Q, 'Q')
