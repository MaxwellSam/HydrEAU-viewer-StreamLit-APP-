#!/bin/sh

# API #
export FLASK_ENV=development
python3 ./API/API.py 

# APP #
python3 -m streamlit run ./Interface/app.py 
