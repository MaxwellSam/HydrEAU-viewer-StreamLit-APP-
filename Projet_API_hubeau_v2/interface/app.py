"""
File: app.py
Description: app interface for hydro data obs
Author: Sam Maxwell
Date: 02/2022
"""

import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static 

import data
import variables as var
import toolbox as tb

st.write("")

long = st.number_input('longitude', value=var.long_bordeaux)
lat = st.number_input('latitude', value=var.lat_bordeaux)
dist = st.slider('distance (km)', value=var.dist)

# @st.cache
def fetch_df(long,lat,dist):
    return data.load_data_stations(long,lat,dist)

df = fetch_df(long, lat, dist)

# st.dataframe(data.load_data_stations(long,lat,dist))
st.dataframe(df)
st.write(var.generate_url_coord(long,lat,dist))

# my_map = folium.Map(location = [var.lat_bordeaux,var.long_bordeaux], zoom_start = 13)
# for i in df.index:
#     coord = [df["latitude_station"][i], df["longitude_station"][i]]
#     popup = "code station: {}".format(df["code_station"][i])
#     folium.Marker(
#        location=coord, 
#        popup=popup
#     ).add_to(my_map)

my_map = tb.creat_map(df)

folium_static(my_map)

# Initialization
if 'x' not in st.session_state:
    st.session_state['x'] = 0

x = 0 
if st.button('x+=1'):
    st.session_state.x+=1
if st.button('x+=2'):
    st.session_state.x+=2
st.write(st.session_state.x)