# HydrEAUviewer StreamLitAPP

HydrEAUviewer StreamLitAPP is a Web Application developed in python with StreamLit.
This App use an overlayer API to get hydrological data from HubEAU, an online API for water data ([hubEAU](https://hubeau.eaufrance.fr/)).
This tool allow to visualize three parameters, water tide, flow and daily flow regitred from hydrological stations located at a variable distance of a coordinates point.   

## Overview

![view Web APP](img/Screenshot%202022-02-23%20at%2017.26.27.png)

## Python Dependancies

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

### Install requirements

#### With virtualenv

```
virtualenv .venv
source ./.venv/bin/activate
pip3 install update pip
pip3 install -r requirements.txt
```

#### or with conda

```
 conda create --prefix ./venv python=3.8
 conda activate ./.venv
 pip3 install udate pip
 pip3 install -r requirements.txt
```

## Run the app

### With run.sh

```
sh run.sh
```

### Or directly with python

```
python3 ./API/API.py
python3 -m streamlit run ./Interface/app.py
```

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
 
1) run the API

The folder **./API** contain code about for the overlayer API.
  
For using the developer mode, run the command:
- Windows env: `$env:FLASK_ENV = "development"`
- Mac/Linux env: `export FLASK_ENV=development`

To run the API, use the command `python3 ./API/API.py`

2) run the APP   

To run the APP, use the command `python3 -m streamlit run ./Interface/app.py` 

### Or use run.sh 

Execute this command in a shell bash `sh run.sh`

*<u>note:</u> to run python script this file use the variable ***python3***, or if this one is not found it will try with the varibale ***python***. Then, be sure you have this variables in your env and they are pointing on the right python version.*  