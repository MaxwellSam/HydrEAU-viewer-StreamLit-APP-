"""
File: toolbox.py
Description: contain tools methods for APP
Author: Sam Maxwell
Date: 02/2022
"""

import variables as var
import folium
import streamlit as st
import matplotlib.pyplot as plt 

# mapping

# @st.cache
def creat_map(df, station_selected, stations_available, coord_center):
    # my_map = folium.Map(location = [var.default_lat,var.default_long], zoom_start = 10)
    my_map = folium.Map(location = coord_center, zoom_start = 10)
    for i in df.index:
        coord = [df["latitude_station"][i], df["longitude_station"][i]]
        popup = "{}\n\n ({})".format(df["libelle_station"][i], df["code_station"][i])
        if df.libelle_station[i] == station_selected:
            folium.Marker(
                location=coord, 
                popup=popup,
                icon =folium.Icon(color="blue")
                ).add_to(my_map)
        elif df.libelle_station[i] in stations_available:
            folium.Marker(
                location=coord, 
                popup=popup,
                icon =folium.Icon(color="green")
                ).add_to(my_map)
        else:
            folium.Marker(
                location=coord, 
                popup=popup,
                icon =folium.Icon(color="red")
                ).add_to(my_map)
        # folium.Marker(
        #     location=coord, 
        #     popup=popup,
        #     icon =folium.Icon(color="red")
        #     ).add_to(my_map)
    return my_map

def plot_data_station(dataframe, station):
    df = dataframe[dataframe.libelle_station == station]

    fig, ax = plt.subplots()
    ax.set_xlabel("date")
    ax.set_ylabel("Q")
    df.plot(kind="line", x="date_obs_elab", y="resultat_obs_elab", ax=ax)
    ax.grid(axis='x', color='0.80')
    return fig