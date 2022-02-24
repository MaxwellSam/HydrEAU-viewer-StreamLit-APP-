#!/bin/sh

export FLASK_ENV=development

{ # if variable python3 exist
    python3 ./API/API.py & # run API
    python3 -m streamlit run ./Interface/app.py # run APP 
}|| { # else try python variable 
    python ./API/API.py & 
    python -m streamlit run ./Interface/app.py
}
 
