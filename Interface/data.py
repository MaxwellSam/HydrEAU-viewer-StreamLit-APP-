"""
File: data.py
Description: contain methods to construct dataset
Author: Sam Maxwell
Date: 02/2022
"""

import streamlit as st
import Interface.variables as var
import pandas as pd
import json 
import requests

#####################################################################################################
#                                        STATIONS                                                   #
#####################################################################################################

@st.cache
def fetch_data(url):
    """
    Description: request the API with the url and return the response as text format 
    input: 
        url: 
            type: str
            desc: url for requestinf API
    output : 
        resp.text: 
            type: str
            desc: data json as text format returned by the API  
    """
    resp = requests.get(url)
    print("#####\n")
    print(url)
    print(resp)
    print("\n#####")
    return resp.text

def load_data_stations(long, lat, dist):
    """
    Description: load data stations from the API around the specified distance (dist) from the specified coordinate (long, lat).
    input: 
        long: 
            type: float
            desc: longitude
        lat:
            type: float
            desc: latitude
        dist:
            type: int
            desc: distance (in km) around the coordinates
    output :  
            type: dataframe
            desc: dataframe which contain stations info at dist around [long, lat]  
    """
    if long == 0 or lat == 0 or dist == 0:
        tmp = fetch_data(var.url_hydro_stations)
        print(var.url_hydro_stations)
    else:
        tmp = fetch_data(var.generate_url_coord(long, lat, dist))
    data_json = json.loads(tmp)
    return pd.DataFrame.from_dict(data_json, orient='index')

#####################################################################################################
#                                        HYDRO OBS                                                  #
#####################################################################################################

############# 
# Hydro Obs #
#############

def load_data_hydro_obs_elab(stations, days_before):
    """
    Description: load the data hydro elaborate (daily flow "QmJ") with a specified data history (days_before)  
    input: 
        stations: 
            type: dataframe 
            desc: contain info about stations
        days_before:
            type: int
            desc: number of days before the curent date
    output : 
        df: 
            type: dataframe
            desc: contain hydro data of stations specified 
    """
    url = var.generate_url_hydro_obs_elab(stations, days_before)
    tmp = fetch_data(url)
    json_data = json.loads(tmp)
    df = pd.DataFrame.from_dict(json_data, orient='index')
    df = df.rename(columns={"date_obs_elab":"date_obs", "resultat_obs_elab":"QmJ"})
    return df

################ 
# Hydro Obs tr #
################

def creat_df_tr_from_url(url, hydro_mesure):
    """
    Description: creat dataframe of "real time" data according to the hydro measure (distinction between "H" and "Q")
    input: 
        url: 
            type: str
            desc: url base for requesting API (just have to specified the hydro measure)
        hydro_measure:
            type: str
            desc: type of hydro measure ("H" or "Q")
    output : 
        df: 
            type: dataframe
            desc: contain data hydro "real time" of stations for the hydro measure specified  
    """
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


def load_data_hydro_obs_tr(stations, days_before):
    ## stations ##
    # df_stations = load_data_stations(long, lat, dist)
    # stations = df_stations.code_station.tolist()
    ## data hydro tr ##
    url_H = var.generate_url_hydro_obs_tr_H(stations, days_before)
    url_Q = var.generate_url_hydro_obs_tr_Q(stations, days_before)
    df_H = creat_df_tr_from_url(url_H, 'H')
    df_Q = creat_df_tr_from_url(url_Q, 'Q')
    return pd.merge(df_H, df_Q, how='outer')

def load_data_hydro_obs_tr_H(stations, days_before):
    """
    Description: load data water tide ("H") in "real time" for the specified stations and with the specific history of days 
    input: 
        stations: 
            type: dataframe 
            desc: contain info of stations
        days_before:
            type: int
            desc: number of days before the curent date
    output : 
            type: dataframe
            desc: contain info of water tide reccorded by the stations since days_before 
    """
    ## stations ##
    # df_stations = load_data_stations(long, lat, dist)
    # stations = df_stations.code_station.tolist()
    ## data hydro tr ##
    url_H = var.generate_url_hydro_obs_tr_H(stations, days_before)
    return creat_df_tr_from_url(url_H, 'H')

def load_data_hydro_obs_tr_Q(stations, days_before):
    """
    Description: load data water flow ("Q") in "real time" for the specified stations and with the specific history of days 
    input: 
        stations: 
            type: dataframe 
            desc: contain info of stations
        days_before:
            type: int
            desc: number of days before the curent date
    output : 
            type: dataframe
            desc: contain info of water flow reccorded by the stations since days_before 
    """
    ## stations ##
    # df_stations = load_data_stations(long, lat, dist)
    # stations = df_stations.code_station.tolist()
    ## data hydro tr ##
    url_Q = var.generate_url_hydro_obs_tr_Q(stations, days_before)
    return creat_df_tr_from_url(url_Q, 'Q')

############################ 
# check stations with data #
############################

def get_stations_with_data(hydro_measure, stations):
    """
    Description: filter stations dataframe to return only stations which have data of hydro measure ("Q", "H" or "QmJ") 
    input: 
        hydro_measure:
            type: str
            desc: type of hydro measure ("H", "Q" or "QmJ")
        stations: 
            type: dataframe 
            desc: contain info about stations
    output : 
            type: dataframe
            desc: contain info of water tide reccorded by the stations since days_before 
    """
    codes_stations = stations.code_station.tolist()
    if hydro_measure == "Q":
        df = load_data_hydro_obs_tr_Q(codes_stations, 1)
    elif hydro_measure == "H":
        df = load_data_hydro_obs_tr_H(codes_stations, 1)
    elif hydro_measure == "QmJ":
        df = load_data_hydro_obs_elab(codes_stations, 1)
    else: 
        return None
    return stations[stations.code_station.isin(df.code_station)]

################################### 
# Generate Dataframe Hydro (auto) #
###################################

def get_data_hydro_station(station_selected, hydro_measure, stations, days_before):
    """
    Description: get dataframe of a stecific station for a specific hydro measure ("Q", "H" or "QmJ") with a data history (days_before) 
    input: 
        station_selected:
            type: str
            desc: libelle of the selected station
        hydro_measure:
            type: str
            desc: type of hydro measure ("H", "Q" or "QmJ")
        stations: 
            type: dataframe 
            desc: contain info about stations
        days_before:
            type: int
            desc: number of days before the curent date
    output : 
        df:
            type: dataframe
            desc: contain data hydro ("Q", "H" or "QmJ") reccorded by the station since the number of days "days_before" 
    """
    code_station = stations[stations.libelle_station == station_selected].code_station.tolist()
    if hydro_measure == "Q":
        df = load_data_hydro_obs_tr_Q(code_station, days_before)
    elif hydro_measure == "H":
        df = load_data_hydro_obs_tr_H(code_station, days_before)
    elif hydro_measure == "QmJ":
        df = load_data_hydro_obs_elab(code_station, days_before)
    else: 
        return None
    return df


