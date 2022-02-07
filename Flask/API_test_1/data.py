import numpy as np
import pandas as pd 

# Variables 

filePATH = "./data_2020-04.csv"

# Methods 

def filter_region(region_name, dataframe):
    return df[df["region"]==region_name]

# Dataframes 

df = pd.read_csv(filePATH, sep=',')
df_groupby = df.groupby(["region", "day"]).mean()
df_index = df.set_index(["region", "day"])

