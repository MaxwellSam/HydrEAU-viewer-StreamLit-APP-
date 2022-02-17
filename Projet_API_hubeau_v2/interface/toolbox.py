"""
File: toolbox.py
Description: contain tools methods for APP
Author: Sam Maxwell
Date: 02/2022
"""

import variables as var
import folium
import streamlit as st

# mapping

# @st.cache
def creat_map(df):
    my_map = folium.Map(location = [var.default_lat,var.default_long], zoom_start = 10)
    for i in df.index:
        coord = [df["latitude_station"][i], df["longitude_station"][i]]
        popup = "code station: {}".format(df["code_station"][i])
        folium.Marker(
           location=coord, 
           popup=popup
        ).add_to(my_map)
    return my_map