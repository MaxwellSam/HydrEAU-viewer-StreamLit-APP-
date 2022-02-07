import requests
import pandas as pd
import json

# Methods

def url_to_dataframe(url):
    """
    convert url reponse to json and convert json to return pandas dataframe 
    """ 
    resp = requests.get(url)
    data_json = json.loads(resp.text)
    return pd.DataFrame.from_dict(data_json, orient="index").set_index(["region", "day"])

"""
===============================================================
                             Test
===============================================================
"""
# note: the API apply.py must be run before running this script

# Test 1: Get Bretagne's data 

url_Bretagne = "http://127.0.0.1:5000/REGION/Bretagne"
df_Bretagne = url_to_dataframe(url_Bretagne)
print(df_Bretagne)

# Test 2: Get Nouvelle-Aquitaine's data

url_N_Aquitaine = "http://127.0.0.1:5000/REGION/Nouvelle-Aquitaine"
df_Aquitaine = url_to_dataframe(url_N_Aquitaine)
print(df_Aquitaine)