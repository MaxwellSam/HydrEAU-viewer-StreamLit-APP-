import numpy as np
import pandas as pd 

# Variables 

filePATH = "./data_2020-04.csv"

# Methods 

def filter_region(region_name, dataframe):
    return dataframe[dataframe["region"]==region_name]

# Dataframes 

df = pd.read_csv(filePATH, sep=',')
## extract list of regions in dataframe without duplicates values
list_region = list(set(df["region"].values))

df_groupby = df.groupby(["region", "day"]).mean()
df_index = df.set_index(["region", "day"])

df
