import streamlit as st
import pandas as pd
import data
import variables as var

st.write("")

long = st.number_input('longitude', value=var.long_bordeaux)
lat = st.number_input('latitude', value=var.lat_bordeaux)
dist = st.slider('distance (km)', value=var.dist)

st.dataframe(data.load_data_stations(long,lat,dist))
st.write(var.generate_url_coord(long,lat,dist))