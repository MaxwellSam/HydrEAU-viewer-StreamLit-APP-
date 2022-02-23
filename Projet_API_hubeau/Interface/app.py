"""
File: app.py
Description: app interface for hydro data obs
Author: Sam Maxwell
Date: 02/2022
"""

# --------------------------------- Imports --------------------------------
import stat
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static 
import matplotlib.pyplot as plt 

import data
import variables as var
import toolbox as tb

# ------------------------------- Page config -------------------------------
apptitle = "hydrEAU viewer"
icone = "https://img.icons8.com/external-flaticons-flat-flat-icons/64/000000/external-water-astrology-flaticons-flat-flat-icons.png"
st.set_page_config(
    apptitle, 
    icone,
    # layout="wide",
    initial_sidebar_state="expanded")

# --------------------------------- Sidebar  --------------------------------

# Inputs #
#--------#

s = st.sidebar
s.write( 
    """
    
    # Parameters

    ## Coordinate  
    """
    )

## coordinate ## 

long = s.number_input('longitude', value=var.long_bordeaux)
lat = s.number_input('latitude', value=var.lat_bordeaux)

## Distance ##

dist = s.slider('distance (km)', value=var.dist)

## Hydro measure ##

s.write("## Data parameters")

hydro_measure = s.selectbox(
    "hydrometric measure",
    var.Hydro_measure_to_DF_columns.keys(),
    format_func= var.get_hydro_measure_selected
)

## data history ##

days_before = s.slider('Data history (in days)', value=var.days_before_default, min_value=1, max_value=25)

## session state test ##

if 'x' not in st.session_state:
    st.session_state['x'] = 0

s.write("## Test session_state")

if s.button('x+=1'):
    st.session_state.x+=1
if s.button('x+=2'):
    st.session_state.x+=2

s.write("x = {}".format(st.session_state.x))

# --------------------------------- Dataframes  ------------------------------

## Stations ##

stations = data.load_data_stations(long,lat,dist)
codes_stations = stations.code_station.tolist()
stations_with_data = data.get_stations_with_data(hydro_measure, stations)

## Select Input Station ## 

station_selected = st.selectbox(
    "Select station",
    # df3_stations_with_data.code_station.tolist()
    stations_with_data.libelle_station
)

## Dataframe hydro ## 

data_station_selected = data.get_data_hydro_station(station_selected, hydro_measure, stations_with_data, days_before)

# ## Data hydro

# # st.write(var.generate_url_hydro_obs_tr_H(df_stations.columns.tolist(), days_before))

# df_data_obs_elab = data.load_data_hydro_obs_elab(codes_stations, days_before)
# # st.dataframe(df2_data_obs_elab)
# df_data_obs_tr = data.load_data_hydro_obs_tr(codes_stations, days_before)
# df_data_obs_tr_H = data.load_data_hydro_obs_tr_H(codes_stations, days_before)
# df_data_obs_tr_Q = data.load_data_hydro_obs_tr_Q(codes_stations, days_before)
# # st.write(df3_data_obs_tr)

# df_stations_with_data_elab = stations[stations["code_station"].isin(df_data_obs_elab["code_station"])]
# df_final_df_elab = pd.merge(df_stations_with_data_elab, df_data_obs_elab)

# df_stations_with_data_tr = stations[stations["code_station"].isin(df_data_obs_tr["code_station"])]
# df_final_tr = pd.merge(df_stations_with_data_tr, df_data_obs_tr)

# # st.dataframe(df2_data_obs.set_index(["code_station"]).sort_index())

# list_df = [df_data_obs_elab, df_data_obs_tr_H, df_data_obs_tr_Q]

# for df in list_df: 
#     if hydro_measure in df.columns:
#         df_selected = df.merge(stations)
#         df_selected["date_obs"] = pd.to_datetime(df_selected["date_obs"])
#         stations_with_data = stations[stations["code_station"].isin(df_selected["code_station"])]
#         break


# my_map = folium.Map(location = [var.lat_bordeaux,var.long_bordeaux], zoom_start = 13)
# for i in df.index:
#     coord = [df["latitude_station"][i], df["longitude_station"][i]]
#     popup = "code station: {}".format(df["code_station"][i])
#     folium.Marker(
#        location=coord, 
#        popup=popup
#     ).add_to(my_map)

# --------------------------------- Map ---------------------------------------

my_map = tb.creat_map(stations, station_selected, stations_with_data.libelle_station.tolist(),[lat, long])

folium_static(my_map)

# --------------------------------- Graph ---------------------------------------

# st.pyplot(tb.plot_data_station(hydro_measure, df_selected, station_selected))
# st.plotly_chart(tb.plot_data_station_plotly(hydro_measure, df_selected, station_selected))
st.plotly_chart(tb.plot_data_station_plotly(hydro_measure, data_station_selected, station_selected))

# -------------------------- controle dataframe ---------------------------------
with st.expander("See dataframe"):
    st.write("##### {} Stations found at {} km around the coordinates {} ; {}".format(len(stations),dist, long, lat))
    st.dataframe(stations)

# st.write("#### obs elab")
# st.write("##### Hydro observation elab data")
# st.dataframe(df_data_obs_elab)
# st.write("##### Stations with records (total = {} stations)".format(len(df_stations_with_data_elab)))
# st.dataframe(df_stations_with_data_elab)
# st.write("##### Final dataframe")
# st.dataframe(df_final_df_elab)

# st.write("#### obs str")
# st.write("##### Hydro observation elab data")
# st.dataframe(df_data_obs_tr)
# st.write("##### Stations with records (total = {} stations)".format(len(df_stations_with_data_tr)))
# st.dataframe(df_stations_with_data_tr)
# st.write("##### Final dataframe")
# st.dataframe(df_final_tr)

# st.write("#### obs str")
# st.write("##### Hydro observation elab data")
# st.dataframe(df_data_obs_tr)
# st.write("##### Stations with records (total = {} stations)".format(len(df_stations_with_data_tr)))
# st.dataframe(df_stations_with_data_tr)
# st.write("##### Final dataframe")
# st.dataframe(df_final_tr)

    st.write("### Dataframe hydro")
    st.write("#### measure: {}".format(var.Hydro_measure_to_DF_columns[hydro_measure]))
    st.write("stations with data: {}".format(len(stations_with_data)))
    st.dataframe(stations_with_data)
    st.write("#### Dataframe selected station: {}".format(station_selected))
    st.dataframe(data_station_selected)
