import os
import shutil
import json
import glob

'''

Function to concatenate in two different file both  "csv_filter" and "csv_204_error" json files.

Pseudo code:

open the main directory
create two different folder: "csv_filter_folder" & "csv_204_error_folder"

if name file like "csv_filter"
    insert file in "csv_filter_folder" folder
elsif
    insert file in folder "csv_204_error_folder"

open "csv_filter_folder"
write a new file "all_filter.json" with all csv "filter"
write a new file "all_204_error.json" with all csv "204_error"

'''


def main():
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
    with open(path + "/all_200_error.json", "+w") as outfile:
        json.dump(result_filter_204, outfile, indent=2)


'''

Check with the ground truth (Tranco List)

Aim: calculate the FP rate caused by VirusTotal

input : file 'tranco.csv' & 'all_filter.json'

- parse json to dictionary:
    [
        {
            "nome_dominio": [
                {
                    "score": int,
                    "status response": int,
                    "total": int
                }
                                    
            ]
    
        }
    ]
    
    |
    |
    |
    |
   \ /
    '
    { 'nome_dominio' : { 'score': int, 'status': int, 'total': int }}
    
    
- for each entry in the dict -> obtain the key 'nome_dominio' and insert in a new dict ('nome_dom'}
- for entry check the presence in 'tranco.csv' and add 0 or 1 if there is or not (es : (

    
    
'''


def fp_VT(csv_tranco, dict_json_all_filter):
    exit()


if __name__ == "__main__":
    main()
