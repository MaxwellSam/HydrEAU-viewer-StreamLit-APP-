"""
File: variables.py
Description: contain variables for API
Author: Sam Maxwell
Date: 02/2022
"""

# url hubeau

## river temperature 
url_river_temp_station = "https://hubeau.eaufrance.fr/api/v1/temperature/station?format=json"

## hydro
# url_hydro_stations = "https://hubeau.eaufrance.fr/api/v1/hydrometrie/referentiel/stations?en_service=true&format=json"
# url_hydro_obs = "https://hubeau.eaufrance.fr/api/v1/hydrometrie/obs_elab"

# fields_station="fields=code_station,libelle_region,date_fermeture_station,date_ouverture_station,longitude_station,latitude_station"
# url_hydro_stations_filtre = "https://hubeau.eaufrance.fr/api/v1/hydrometrie/referentiel/stations?format=json"+"&%s"%(fields_station)
# url_hydro_stations_filtre = url_hydro_stations+"&%s"%(fields_station)

# fields_hydro_obs = "fields=code_station,date_obs_elab,date_prod,grandeur_hydro_elab,resultat_obs_elab"
# url_hydro_obs_filtred = url_hydro_obs+"?%s"%(fields_hydro_obs)

# conv_key_words_hubeau 
## note: dict to convert keyword from request to keyword for hubeau request


###################################### usefull methods ##############################################

def fields_filter_generator(fields):
    return "fields="+",".join(fields)
        
#####################################################################################################
#                                        STATIONS                                                   #
#####################################################################################################

##################################### Fields Selection ##############################################

station_fields = [
    "code_station",
    "libelle_station",
    "type_station",
    "libelle_commune",
    "libelle_region",
    "date_ouverture_station",
    "longitude_station",
    "latitude_station"
]

####################################### URL variables ###############################################

url_hydro_stations = "https://hubeau.eaufrance.fr/api/v1/hydrometrie/referentiel/stations?en_service=true&format=json"
url_hydro_stations_filtre = url_hydro_stations+"&%s"%(fields_filter_generator(station_fields))

################################# keyword dict translator ###########################################

translate_key_word = {
    "long":"longitude",
    "lat":"latitude",
    "dist":"distance", 
    "stations":"code_entite",
    "date_start_obs":"date_debut_obs_elab",
    "date_end_obs":"date_fin_obs_elab",
    "hydro_type":"grandeur_hydro_elab"
}

translate_timedate = {
    "D":"date_debut_obs_elab",
    "M":"date_debut_obs_elab",
    "Y":"date_debut_obs_elab"
}

#####################################################################################################
#                                        HYDRO OBS                                                  #
#####################################################################################################

##################################### Fields Selection ##############################################

obs_fields = [
    "code_station",
    "date_obs_elab",
    "date_prod",
    "grandeur_hydro_elab",
    "resultat_obs_elab"
]

####################################### URL variables ###############################################

url_hydro_obs = "https://hubeau.eaufrance.fr/api/v1/hydrometrie/obs_elab"
url_hydro_obs_filtred = url_hydro_obs+"?%s"%(fields_filter_generator(obs_fields))
