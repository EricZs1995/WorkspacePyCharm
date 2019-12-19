'''

Script to concatenate in two different file both  "csv_filter" and "csv_204_error" json files.

Pseudocode:

open the main directory
create two different folder: "csv_filter_folder" & "csv_204_error_folder"

if name file like "csv_filter"
    insert file in "csv_filter_folder" folder
elsif
    insert file in folder "csv_204_error_folder"

open "csv_filter_folder"
write a new file "all_filter.json"
write a new file "all_204_error.json"

initialize a flag : flag_filter = true

for each file in "csv_filter_folder"
    if flag_filter:
        flag_filter = false
        remove the last line ("}")
        append in "all_filter.json"
    elsif:
        remove the first line ("{")
        append in "all_filter.json"

initialize a flag : flag_204_error = true

for each file in "csv_204_error_folder"
    if flag_204_error:
        flag_204_error = false
        remove the last line ("}")
        append in "all_204_error"
    else:
        remove the first line ("{")
        append in "all_204_error"

'''

import os
import shutil
from jsonmerge import merge
import json
import glob

path = "/Volumes/PEPPE_DT/WorkspacePyCharm/VirusTotalUmbrellaTop1M/py_prova_merge/prova_merge"
path = os.path.relpath(path)
# print(path)

csv_filter_folder = path + "/csv_filter_folder"
try:
    os.mkdir(csv_filter_folder)
except FileExistsError:
    print("Directory 'filter' already exists")
  
csv_204_error_folder = path + "/csv_204_error_folder"
try:
    os.mkdir(csv_204_error_folder)
except FileExistsError:
    print("Directory '204_error' already exists")


for file in os.listdir(path):
    if "csv_filter" in file:
        shutil.move(path + "/" + file, csv_filter_folder)
    else:
        shutil.move(path + "/" + file, csv_204_error_folder)
'''
try:
    all_filter = open(path + "/all_filter.json", "+w")
except IOError:
    print("Filed to open the 'all_filter' file")
'''

result_filter = []
for f in glob.glob(csv_filter_folder + "/*.json"):
    with open(f, "r") as infile:
        result_filter.append(json.load(infile))
with open(path + "/all_filter.json", "+w") as outfile:
    json.dump(result_filter, outfile, indent=2)

result_filter_204 = []
for f in glob.glob(csv_204_error_folder + "/*.json"):
    with open(f, "r") as infile:
        result_filter_204.append(json.load(infile))
with open(path + "/all_200_error.json") as outfile:
    json.dump(result_filter_204, outfile, indent=2)
