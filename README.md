# HydrEAUviewer StreamLitAPP

HydrEAUviewer StreamLitAPP is a Web Application developed in python with StreamLit.
This App use an overlayer API to get hydrological data from HubEAU, an online API for water data.
This tool allow to visualize three parameters, water tide, flow and daily flow regitred from hydrological stations located at a variable distance of a coordinates point.   

## Overview

![view Web APP](img/Screenshot%202022-02-23%20at%2017.26.27.png)

## Python Dependancy

The program use some python modules. Please assure you to have installed on your python environnment the following modules :
- Data storage and manipulation 
  -  `Pandas`
- Data visualisation
  - `Matplotlib`
  - `Plotly`
  - `Seaborn`
- Mapping
  - `Folium`
  - `Streamlit_folium`
- Web Interface
  - `Streamlit`
- API 
  - `Flask`
  - `Requests` 

## Project Architecture

```
./
  | _ _ API/
  |         | _ API.py
  |         | _ toolbox.py
  |         | _ variables.py 
  |
  | _ _ Interface/
  |         | _ app.py
  |         | _ data.py
  |         | _ toolbox.py
  |         | _ variables.py
  |
  | _ README.md
  | _ img/
```

## Running APP 

To run the APP please follow the steps below

### Windows 

1) run the API

The folder **./API** contain code about for the overlayer API.
  
For using the developer mode, run the command `$env:FLASK_ENV = "development"`
To run the API, use the command `python3 ./API/API.py`

2) run the APP   

To run the APP, use the command `python3 -m streamlit run ./Interface/app.py` 