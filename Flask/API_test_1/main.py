import requests
import pandas as pd
import json

# Methods

def url_region_to_dataframe(url, region):
    """
    convert url reponse to json and convert json to return pandas dataframe 
    """ 
    resp = requests.get(url)
    data_json = json.loads(resp.text)
    return pd.DataFrame.from_dict(data_json[region], orient="index")

"""
===============================================================
                             Test
===============================================================
"""
# note: the API apply.py must be run before running this script

# Test 1: Get Bretagne's data 

url_Bretagne = "http://127.0.0.1:5000/REGION/Bretagne"
df_Bretagne = url_region_to_dataframe(url_Bretagne, "Bretagne")
print(df_Bretagne)

# Test 2: Get Nouvelle-Aquitaine's data

url_N_Aquitaine = "http://127.0.0.1:5000/REGION/Nouvelle-Aquitaine"
df_Aquitaine = url_region_to_dataframe(url_N_Aquitaine, "Nouvelle-Aquitaine")
print(df_Aquitaine)

