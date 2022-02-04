import numpy as np
import pandas as pd 

# Variables 
filePATH = "./data_2020-04.csv"

df = pd.read_csv(filePATH, sep=',', index_col=0)
# print(df)