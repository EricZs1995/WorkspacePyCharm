import os
import shutil
import json
import glob

'''
                                    #######"filter_merge"#######
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


def filter_merge(csv_filter_fold, csv_204_error_fold, string_path_json_filter, string_path_204):

    """
    :param csv_filter_fold: folder with only json ~ "csv_filter"
    :param csv_204_error_fold: folder with only json ~ "csv_204_error"
    :param string_path_json_filter: path where found "all_filter.json"
    :param string_path_204: path where found "all_204_error.json"
    :return:
    """

    result_filter = []
    for f in glob.glob(csv_filter_fold + "/*.json"):
        with open(f, "r") as infile:
            result_filter.append(json.load(infile))
    with open(string_path_json_filter, "+w") as outfile:
        json.dump(result_filter, outfile, indent=2)

    result_filter_204 = []
    for f in glob.glob(csv_204_error_fold + "/*.json"):
        with open(f, "r") as infile:
            result_filter_204.append(json.load(infile))
    with open(string_path_204, "+w") as outfile:
        json.dump(result_filter_204, outfile, indent=2)


'''

                                                ########"fp_vt"########
Check with the ground truth (Tranco List)

Aim: calculate the FP rate caused by VirusTotal

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
    
    
- for each entry in the dict -> obtain the key 'nome_dominio' and insert in a new dict {'nome_dom'}
- for entry check the presence in 'tranco.csv' and add 0 or 1 if there is or not (es : {'nome_dom': 0}

'''


def fp_vt(csv_tranco, json_all_filter_in):

    """
    :param csv_tranco: csv of Tranco rank
    :param json_all_filter_in: path of 'all_filter.json'
    :return:
    """
    exit()


if __name__ == "__main__":

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

    path_csv_filter_all = path + "/all_filter.json"
    path_csv_204_error = path + "/all_204_error.json"
    filter_merge(csv_filter_folder, csv_204_error_folder, path_csv_filter_all, path_csv_204_error)

