import pandas as pd
from pandas import DataFrame
from pandas.io.json import json_normalize
import json
import csv
import sys
'''
all_filter_json = "/Volumes/PEPPE_DT/WorkspacePyCharm/VirusTotalUmbrellaTop1M/py_prova_merge/prova_merge/all_200_filter.json"
with open(all_filter_json) as file:
    json_data = json.load(file)
print(type(json_data))
print(json_data[0][0])
#print(json_data)
'''
'''
df = pd.DataFrame.from_dict(json_data, orient="index")
print(df)
'''


''' problema file concatenati--> presenza di ',' nel file finale di concatenazione '''

xaa_json = "/Volumes/PEPPE_DT/WorkspacePyCharm/VirusTotalUmbrellaTop1M/py_prova_merge/prova_merge/csv_204_error_folder/xaa.csv_204_error.json"

with open(xaa_json) as file:
    json_data = json.load(file)

print(json_data.items())


df = pd.DataFrame.from_dict(json_data)
#print(df.T)
dft = df.T
