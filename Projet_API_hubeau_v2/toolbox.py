"""
File: toolbox.py
Description: contain tool's methods
Author: Sam Maxwell
Date: 02/2022
"""

import requests
import pandas as pd 
import json

import variables as var

def url_hubeau_to_json(url):
    response = requests.get(url, verify=False)
    return json.loads(response.text)


"""
----------------------------------------------------------
                    Creating Request for hubEAU
----------------------------------------------------------
"""

# parser request API: 

hydro_request_to_url()
    