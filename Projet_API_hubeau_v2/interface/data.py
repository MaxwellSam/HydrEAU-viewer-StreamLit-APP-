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

@st.cache
def generate_dataframe(url):
    resp = requests.get(url)
    data_json = json.loads(resp.text)
    return pd.DataFrame.from_dict(data_json["data"])
    # return pd.DataFrame.from_dict(data_json)



def load_data_stations(long, lat, dist):
    if long == 0 or lat == 0 or dist == 0:
        return generate_dataframe(var.url_hydro_stations)
    else:
        return generate_dataframe(var.generate_url_coord(long, lat, dist))

