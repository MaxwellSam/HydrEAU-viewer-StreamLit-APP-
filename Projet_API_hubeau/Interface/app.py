"""
File: app.py
Description: app interface for hydro data obs
Author: Sam Maxwell
Date: 02/2022
"""

# --------------------------------- Imports --------------------------------
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
st.set_page_config(apptitle, icone)

# --------------------------------- Sidebar  --------------------------------

s = st.sidebar
s.write(
    """
    # Parameters

    ## Coordinate  
    """
    )
long = s.number_input('longitude', value=var.long_bordeaux)
lat = s.number_input('latitude', value=var.lat_bordeaux)
dist = s.slider('distance (km)', value=var.dist)
s.write("## Data parameters")
days_before = s.slider('Data history (in days)', value=var.days_before_default)

# session state test 
if 'x' not in st.session_state:
    st.session_state['x'] = 0

s.write("## Test session_state")
# x = 0 
if s.button('x+=1'):
    st.session_state.x+=1
if s.button('x+=2'):
    st.session_state.x+=2

s.write("x = {}".format(st.session_state.x))

# st.write(data.load_data_hydro_obs(long, lat, dist, days_before))

# --------------------------------- Dataframes  ------------------------------

## Stations 
df1_stations = data.load_data_stations(long,lat,dist)
# st.dataframe(df1_stations)
## Data hydro
df2_data_obs_elab = data.load_data_hydro_obs_elab(long, lat, dist, days_before)
# st.dataframe(df2_data_obs_elab)
df3_data_obs_tr = data.load_data_hydro_obs_tr(long, lat, dist, days_before)
# st.write(df3_data_obs_tr)

df_stations_with_data_elab = df1_stations[df1_stations["code_station"].isin(df2_data_obs_elab["code_station"])]
df_final_df_elab = pd.merge(df_stations_with_data_elab, df2_data_obs_elab)

df_stations_with_data_tr = df1_stations[df1_stations["code_station"].isin(df3_data_obs_tr["code_station"])]
df_final_tr = pd.merge(df_stations_with_data_tr, df3_data_obs_tr)

# st.dataframe(df2_data_obs.set_index(["code_station"]).sort_index())


# my_map = folium.Map(location = [var.lat_bordeaux,var.long_bordeaux], zoom_start = 13)
# for i in df.index:
#     coord = [df["latitude_station"][i], df["longitude_station"][i]]
#     popup = "code station: {}".format(df["code_station"][i])
#     folium.Marker(
#        location=coord, 
#        popup=popup
#     ).add_to(my_map)

# --------------------------------- Map ---------------------------------------
station_selected = st.selectbox(
    """ 
    Select station
    """,
    # df3_stations_with_data.code_station.tolist()
    df_stations_with_data_elab.libelle_station
)
st.write(station_selected)
my_map = tb.creat_map(df1_stations, station_selected, df_final_df_elab["libelle_station"].tolist(),[lat, long])

folium_static(my_map)

# --------------------------------- Graph ---------------------------------------
df_graph = df_final_df_elab[df_final_df_elab.libelle_station == station_selected][["date_obs_elab","resultat_obs_elab"]]

st.pyplot(tb.plot_data_station(df_final_df_elab, station_selected))

# -------------------------- controle dataframe ---------------------------------

st.write("##### Stations found at {} km around the coordinates {} ; {} - nbr stations = {}".format(dist, long, lat, len(df1_stations)))
st.dataframe(df1_stations)
st.write("link API: {}".format(var.generate_url_coord(long,lat,dist)))

st.write("#### obs elab")
st.write("##### Hydro observation elab data")
st.dataframe(df2_data_obs_elab)
st.write("##### Stations with records (total = {} stations)".format(len(df_stations_with_data_elab)))
st.dataframe(df_stations_with_data_elab)
st.write("##### Final dataframe")
st.dataframe(df_final_df_elab)

st.write("#### obs str")
st.write("##### Hydro observation elab data")
st.dataframe(df3_data_obs_tr)
st.write("##### Stations with records (total = {} stations)".format(len(df_stations_with_data_tr)))
st.dataframe(df_stations_with_data_tr)
st.write("##### Final dataframe")
st.dataframe(df_final_tr)