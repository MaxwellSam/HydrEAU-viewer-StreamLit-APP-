import pandas as pd

# methods 
## load local file

def readTXT(path):
    try:
        fileObject = open(path)
        txt = fileObject.read()
        return txt
    except OSError:
        print('cannot open', path)

def readCSV(path):
    return pd.read_csv(path)

# Test 1: text file 

dataTXT = readTXT("./test.txt")
print(dataTXT)

# Test 2: csv file

dataCSV = readCSV("./water_potability.csv")
print(dataCSV)

df_meteo = pd.read_csv("./data_2020-04.csv")




