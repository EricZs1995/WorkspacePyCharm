import pandas as pd
import glob
import  statistics as stat
import numpy as np
import csv

path_prova = "/Volumes/PEPPE_DT/WorkspacePyCharm/VirusTotalUmbrellaTop1M/prova_pandas"
path_100 = "/Volumes/PEPPE_DT/WorkspacePyCharm/VirusTotalUmbrellaTop1M/vt_csv100k/100k.csv"
path_1m = "/Volumes/PEPPE_DT/WorkspacePyCharm/VirusTotalUmbrellaTop1M/vt_csv1m"
path_500 = "/Volumes/PEPPE_DT/WorkspacePyCharm/VirusTotalUmbrellaTop1M/vt_csv500k/500k.csv"
path_folder = "/Volumes/PEPPE_DT/WorkspacePyCharm/VirusTotalUmbrellaTop1M/vt_csv1m/1m.csv"
path_csv_out = "/Volumes/PEPPE_DT/WorkspacePyCharm/VirusTotalUmbrellaTop1M/csv_merge_prova_out.csv"
path_tranco = "/Volumes/PEPPE_DT/WorkspacePyCharm/VirusTotalUmbrellaTop1M/py_prova_merge/tranco-top-1m.csv"

delimiter = ','
tranco_domain = []
with open(path_tranco, 'r') as tranco:
    reader = csv.reader(tranco, delimiter=delimiter)
    for row in reader:
        tranco_domain.append(row[1])

pd.set_option('max_columns', 100)
list_files = []
global_positives = 0
global_positives_0 = 0
global_positives_not_null = 0
global_response_code_0 = 0
count_file = 0
len_list = 0
global_score_positives = {}
list_of_domain_names = []
#list_files = sorted(glob.glob(path_folder+'/x*.csv'))
list_files = sorted(glob.glob(path_100))
for x in list_files:
    count_file += 1
    print("file: " + str(x)+ ' count: ' + str(count_file))
    with open(x) as csvin:
        df = pd.read_csv(x, sep=';')
        list_of_positives = df['positives']
        len_list += len(list_of_positives)
        max_pos = np.nanmax(list_of_positives)
        print("max:" + str(max_pos))
        score_positves = {}
        for x in range(0, int(max_pos) + 1):
            if x == 0:
                eq = sum(z == x for z in list_of_positives)
                print("positives = " + str(x) + ", score= " + str(eq))
                score_positves[str(x)] = eq
                global_positives_0 += eq
            else:
                eq = sum(z == x for z in list_of_positives)
                print("positives = " + str(x) + ", score= " + str(eq))
                score_positves[str(x)] = eq
                global_positives_not_null += eq
        response_code_0 = df['response_code']
        count_response_code_0 = 0
        for x in response_code_0:
            if x == 0:
                count_response_code_0 += 1
        global_response_code_0 += count_response_code_0
        print("Num domains with response code = 0, :" + str(count_response_code_0))
    print("lunghezza dati analizzati: " + str(len_list))
    if count_file == 25:
        break

print("domains with score 0 (good):" + str(global_positives_0))
print("domains with score not null:" + str(global_positives_not_null))
print("domains with response code null:" + str(global_response_code_0))

tranco_dict = {}
first = 0
count = 0
for x in list_files:
    with open(x) as csv_in:
        lines = csv_in.readlines()
        for line in lines:
            if first == 0:
                first = 1
                count += 1
                continue
            else:
                s = line.split(';')
               # print(type(s[1]))
                print(count)
                if s[1] == '1':
                    if s[0] in tranco_domain:
                        tranco_dict[s[0]] = int(s[2])
                else:
                    print("response code = 0")
                count += 1

print(len(tranco_dict.keys()))
score_tranco = {}
values = list(tranco_dict.values())
for x in range(1, int(max_pos) + 1):
    print("in")
    eq = sum(z == x for z in tranco_dict.values())
    print("positives = " + str(x) + ", score= " + str(eq))
    score_tranco[str(x)] = int(eq)
