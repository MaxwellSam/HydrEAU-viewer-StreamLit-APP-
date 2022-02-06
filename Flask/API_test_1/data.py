import numpy as np
import pandas as pd 

# Variables 
filePATH = "./data_2020-04.csv"

df = pd.read_csv(filePATH, sep=',')
# print(df)
# df = pd.read_csv(filePATH, sep=',', index_col=0)
df_groupby = df.groupby(["region", "day"]).mean()
# print(df_groupby)
df_index = df.set_index(["region", "day"])
# print(df_index)
# df = df.groupby("region")
# print(df.groups)
# print(df)

## Filter region 

def filter_region(region_name, dataframe):
    return df[df["region"]=="Bretagne"]
