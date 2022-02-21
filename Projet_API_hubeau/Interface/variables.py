"""
File: variables.py
Description: contain variables for APP
Author: Sam Maxwell
Date: 02/2022
""" 

# route for API
url_API = "http://127.0.0.1:5000/"
url_hydro = url_API+"hydro"
url_hydro_stations = url_hydro+"/stations"
url_hydro_obs_elab = url_hydro+"/obs_elab"
url_hydro_obs_tr = url_hydro+"/obs_tr"

def generate_url_coord(long, lat, dist):
    request_infos = "/coord?long={0}&lat={1}&dist={2}".format(long, lat, dist)
    return url_hydro_stations+request_infos

def generate_url_hydro_obs_elab(stations, days_before):
    request_infos = "?stations={}&D={}".format(",".join(stations), days_before)
    return url_hydro_obs_elab+request_infos

def generate_url_hydro_obs_tr(stations, days_before):
    request_infos = "?stations={}&D={}".format(",".join(stations), days_before)
    return url_hydro_obs_tr+request_infos

# default coordinates :
long_bordeaux = -0.57918
lat_bordeaux = 44.837789
default_long = long_bordeaux
default_lat = lat_bordeaux
## default distance (km)
dist = 30
## default history of data
days_before_default = 5
