"""
File: variables.py
Description: contain variables
Author: Sam Maxwell
Date: 02/2022
"""

# url hubeau
## river temperature 
url_river_temp_station = "https://hubeau.eaufrance.fr/api/v1/temperature/station?format=json"
## hydro
url_hydro_stations = "https://hubeau.eaufrance.fr/api/v1/hydrometrie/referentiel/stations?format=json&size=20"

fields_station="fields=code_station,libelle_region,date_fermeture_station,date_ouverture_station,longitude_station,latitude_station"
url_hydro_stations_filtre = "https://hubeau.eaufrance.fr/api/v1/hydrometrie/referentiel/stations?format=json&size=20"+"&%s"%(fields_station)

# conv_key_words_hubeau 
translate_key_word = {
    "commune":"code_commune_station",
    "departement":"code_departement",
    "region":"code_region" 
}



