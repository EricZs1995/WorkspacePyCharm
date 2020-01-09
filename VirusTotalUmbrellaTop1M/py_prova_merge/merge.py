import os
import shutil
import json
import glob
from jsonmerge import merge
import csv
import time
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt

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
    '''
    result_filter = []
    for f in glob.glob(csv_filter_fold + "/*.json"):
        with open(f, "r") as infile:
            result_filter.append(json.load(infile))
    with open(string_path_json_filter, "+w") as outfile:
        json.dump(result_filter, outfile, indent=2)
    
    '''
    result_filter = {}

    for f in glob.glob(csv_filter_fold + "/*.json"):
        print(f)
        with open(f, "rb") as infile:
            json_data = json.loads(infile.read())
            result_filter.update(merge(result_filter, json_data))

    with open(string_path_json_filter, "+w") as outfile:
        json.dump(result_filter, outfile, indent=2)

    # result_filter_204 = {}

    '''
    for f in glob.glob(csv_204_error_fold + "/*.json"):
        with open(f, "r") as infile:
            result_filter_204.append(json.load(infile))
    with open(string_path_204, "+w") as outfile:
        json.dump(result_filter_204, outfile, indent=2)
    '''
    '''
    for f in glob.glob(csv_204_error_fold + "/*.json"):
        print(f)
        with open(f, "rb") as infile:
            json_data = json.loads(infile.read())
            result_filter_204.update(merge(result_filter_204,json_data))

    with open(string_path_204, "+w") as outfile:
        json.dump(result_filter_204, outfile, indent=2)
    
    '''


'''

                                                ########"fp_vt"########
Check with the ground truth (Tranco List)

Aim: calculate the FP rate caused by VirusTotal

- parse json to dict:
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
  'nome_dominio', [{'score': int, 'status response': int, 'total': int}]
    
    
- for each name in 'tranco' file check if a domain name is in 'all_filter' and have a 'score' > 0 

'''


def fp_vt(tranco_csv, all_filter_json):
    """
    :param tranco_csv: csv of Tranco rank
    :param all_filter_json: path of 'all_filter.json'
    :return:
    """
    with open(all_filter_json) as file_json:
        json_data = json.load(file_json)

    '''
    list of domain name scanned (key values of dict 'json_data')
    '''
    index = []
    for a in json_data.items():
        index.append(a[0])

    index_len = len(index)
    '''
    keep second column of tranco csv
    '''
    delimiter = ','
    tranco_domain = []
    with open(tranco_csv, 'r') as tranco:
        reader = csv.reader(tranco, delimiter=delimiter)
        for row in reader:
            tranco_domain.append(row[1])

    '''
     - check the presence of domain name in tranco csv with a score number > 0, and add them to a new dict.
     - calulate the time to analyse 
    '''
    start = datetime.now()
    fp_dict = {}
    score_l = []
    all_score_not_null = {}
    for x in index:
        for p in json_data[x]:
            if p['score'] > 0:
                # dict : domain with score not null
                all_score_not_null[x] = p['score']
                print(x)
                for dom in tranco_domain:
                    if dom == x:
                        # dict : domain with score not null and in tranco csv
                        fp_dict[x] = p['score']
                        score_l.append(p['score'])
    end = datetime.now()
    for x, y in fp_dict.items():
        print(x, y)

    print('Duration: {}'.format(end - start))
    print(len(index))
    print(len(fp_dict))
    percent = (len(fp_dict) / len(index))
    print("% :" + str(percent * 100))
    maximum = max(score_l)
    print("Max score: " + str(maximum))

    if index_len <= 100000:
        try:
            with open("100K_vt.csv", "w", newline="") as out:
                writer_vt = csv.writer(out)
                for key,value in fp_dict.items():
                    writer_vt.writerow([key,value])
        except IOError:
            print("I/O error vt write csv out 100")
        try:
            with open("100K_full.csv","w", newline="") as out:
                writer_vt = csv.writer(out)
                for key, value in all_score_not_null.items():
                    writer_vt.writerow([key,value])
        except IOError:
            print("I/O error fill write csv out 100")
    elif 100000 < index_len <= 500000:
        try:
            with open("500K_vt.csv", "w", newline="") as out:
                writer_vt = csv.writer(out)
                for key, value in fp_dict.items():
                    writer_vt.writerow([key,value])
        except IOError:
            print("I/O error vt write csv out 500")
        try:
            with open("500K_full.csv","w", newline="") as out:
                writer_vt = csv.writer(out)
                for key,value in all_score_not_null.items():
                    writer_vt.writerow([key,value])
        except IOError:
            print("I/O error fill write csv out 500")
    else:
        try:
            with open("1m_vt.csv", "w", newline="") as out:
                writer_vt = csv.writer(out)
                for key, value in fp_dict.items():
                    writer_vt.writerow([key,value])
        except IOError:
            print("I/O error vt write csv out 1m")
        try:
            with open("1m_full.csv","w", newline="") as out:
                writer_vt = csv.writer(out)
                for key, value in all_score_not_null.items():
                    writer_vt.writerow([key,value])
        except IOError:
            print("I/O error fill write csv out 1m")
    '''
    calculate number of occurrences per score from dict obtained by check with trunco
    '''
    data_plot = {}
    for x in range(1, maximum + 1):
        eq = sum(num == x for num in score_l)
        print("Num of score equal to " + str(x) + " is :" + str(eq))
        data_plot[str(x)] = eq

    '''
    fig_100K, ax1 = plt.subplots()
    ax1.set_title('Basic Plot')
    ax1.boxplot(score_l)
    plt.show()
    '''
    '''
    names = list(data_plot.keys())
    values = list(data_plot.values())
    fig, ax = plt.subplots()
    ax.bar(names, values)

    if index_len <= 100000:
        fig.suptitle("100K bar plot")
    elif 100000 < index_len <= 500000:
        fig.suptitle("500k bar plot")
    else:
        fig.suptitle("1m bar plot")

    plt.show()
    '''


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
    tranco_path = "/Volumes/PEPPE_DT/WorkspacePyCharm/VirusTotalUmbrellaTop1M/py_prova_merge/tranco-top-1m.csv"
    fp_vt(tranco_path, path_csv_filter_all)
