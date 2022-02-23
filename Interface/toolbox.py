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
import matplotlib.dates as mdates
import seaborn as sns
import plotly.express as px
import plotly.graph_objs as go

#----------------------------------- mapping -------------------------------------#

def creat_map(df, station_selected, stations_available, coord_center):
    """
    Description: creat the map with markers are stations found around the coordinates. 
                 A color code is used to identify stations which data are available (green) 
                 or not (red), and the station selected (blue)
    input: 
        df:
            type: dataframe
            desc: contain infos about stations found around the coordinate
        station_selected:
            type: str
            desc: libelle of the selected station
        stations_available:
            type: list <str>
            desc: list of stations with data
        coord_center: 
            type: list <float>
            desc: coordinate to use as center of the map
    output : 
        my_map:
            type: folium object
            desc: map to display 
    """
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
    return my_map

# def plot_data_station(hydro_measure, dataframe, station):
#     df = dataframe[dataframe.libelle_station == station]
#     # date = df["date_obs"]
#     # value = df[hydro_measure]

#     fig, ax = plt.subplots()
#     # ax.set_xlabel("date")
#     # ax.set_ylabel("Q")
#     df.plot(kind="line", x="date_obs", y=hydro_measure, ax=ax)
#     ax.grid(axis='x', color='0.80')
#     # plt.gcf().autofmt_xdate
#     return fig

#----------------------------------- plotting -------------------------------------#

def plot_data_station(hydro_measure, dataframe_selected, station_selected):
    fig = plt.figure()
    sns.lineplot(x="date_obs", y=hydro_measure, data=dataframe_selected)
    plt.xticks(rotation=15)
    return fig

# def plot_data_station_plotly(hydro_measure, dataframe_selected, station_selected):
#     df = dataframe_selected[dataframe_selected.libelle_station == station_selected]
#     fig = px.line(
#         df, 
#         x="date_obs", 
#         y=hydro_measure,
#         hover_data={"date_obs": "|%B %d, %Y"})
#     fig.update_xaxes(
#         dtick="M1",
#         tickformat="%b\n%Y")
#     return fig

def plot_data_station_plotly(hydro_measure, dataframe_selected, station_selected):
    """
    Description: creat the plot of data hydro for the station with plotly
    input: 
        hydro_measure:
            type: str
            desc: type of hydro measure ("H", "Q" or "QmJ")
        dataframe_selected:
            type: dataframe
            desc: contain data hydro of the station 
        station_selected:
            type: str
            desc: libelle of the selected station
    output : 
        fig:
            type: object plotly
            desc: line plot to display 
    """
    df = dataframe_selected # dataframe_selected[dataframe_selected.libelle_station == station_selected]
    fig = go.Figure(go.Scatter(
        x=df["date_obs"], 
        y=df[hydro_measure]))
    return fig
