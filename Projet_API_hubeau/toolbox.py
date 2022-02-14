"""
File: toolbox.py
Description: contain tool's methods
Author: Sam Maxwell
Date: 02/2022
"""

import requests
import pandas as pd 
import json

def url_hubeau_to_json(url):
    response = requests.get(url)
    return json.loads(response.text)