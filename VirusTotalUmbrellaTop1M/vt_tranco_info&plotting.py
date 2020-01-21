import sys
import os
from datetime import datetime,timedelta
import csv
import  pandas as pd
import matplotlib.pyplot as plt
import numpy as np

'''
path_csv_out = "/Volumes/PEPPE_DT/WorkspacePyCharm/VirusTotalUmbrellaTop1M/csv_merge_prova_out.csv"
dict_dom_response = {}
dict_dom_no_response = {}
count = 0
first = 0

with open(path_csv_out, newline='') as csv_in:
    line = csv_in.readlines()
    for x in line:
        if first == 0:
            first = 1
            continue
        else:
            print(count)
            s = x.split(';')
            print(type(s[1]))
            print(type(s[2]))
            if s[1] == '1':
                dict_dom_response[str(s[0])] = int(s[2])
            else:
                dict_dom_no_response[str(s[0])] = 'null'
            count += 1





for x,y in dict_dom_response.items():
    print('chiave :' + str(x) + ', valore:' + str(y))

for x,y in dict_dom_no_response.items():
    print('chiave:' + str(x) + 'valore : ' + str(y))

print('lungh no null :' + str(len(dict_dom_response.keys())))
print('lungh null :' + str(len(dict_dom_no_response.keys())))
print(count)

'''

'''
len_value = [2859, 72806, 89958]
label_x = ["100k", "500k", "1m"]
plt.plot(label_x, len_value)
plt.suptitle("detection line")
plt.savefig("/Volumes/PEPPE_DT/WorkspacePyCharm/VirusTotalUmbrellaTop1M/imagev2/lineplot_det.eps")
plt.show()
'''


width = 0.3
labels = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14']
r_base = np.arange(len(labels))
r_spaz = [x + width for x in r_base]
full_values_100 = [67846,13766,6334,1168,495,226,83,39,17,6,3,1,0,1]
tranco_values_100 = [6543,1323,324,261,133,83,33,12,6,2,0,0,0,0]

plt.bar(r_base, full_values_100, width, label="vt_on_full", log = True)
plt.bar(r_spaz, tranco_values_100, width, label="False_positives")
plt.xticks([r + width for r in range(len(labels))], labels)
plt.yscale("log")
plt.legend()
plt.suptitle("1m")
plt.savefig("/Volumes/PEPPE_DT/WorkspacePyCharm/VirusTotalUmbrellaTop1M/imagev2/barFullTranco1m.eps")
plt.show()


'''
path_csv = "/Volumes/PEPPE_DT/WorkspacePyCharm/VirusTotalUmbrellaTop1M/vt_csv1m/1m.csv"
path_tranco = "/Volumes/PEPPE_DT/WorkspacePyCharm/VirusTotalUmbrellaTop1M/py_prova_merge/tranco-top-1m.csv"

delimiter = ','
tranco_domain = []
with open(path_tranco, 'r') as tranco:
    reader = csv.reader(tranco, delimiter=delimiter)
    for row in reader:
        tranco_domain.append(row[1])

dict_restrict = {}
count_l = 0
first = 0
'''
#ricavo da csv in tutti i domini con response code e positives non nullo e li metto in un dizionario
'''
with open(path_csv) as csv_in:
    lines = csv_in.readlines()
    for line in lines:
        if first == 0:
            first = 1
            count_l += 1
        else:
            s = line.split(';')
            if str(s[2]) == 'null' or str(s[2]) == '0':
                print("response code 0 or good, domain: " + str(s[0]))
                count_l += 1
                continue
            else:
                print(""+str(count_l) + " " + s[0])
                dict_restrict[str(s[0])] = int(s[2])
                count_l += 1

'''
#prenod i nomi di dominio da tale dizionario e li confronto con quelli di tranco, considerando solo quelli con positive diverso da 0
'''
chiavi = list(dict_restrict.keys())

dict_tranco = {}
count = 0
for k in chiavi:
    if k in tranco_domain:
        if dict_restrict[str(k)] != 0:
            print(str(k) + " , yes")
            dict_tranco[str(k)] = dict_restrict[str(k)]
        else:
            print(str(k) + "score 0")


valori_tranco = list(dict_tranco.values())

for x in range(0,17):
    print(x)
    eq = sum(z == x for z in valori_tranco)
    print("values = " + str(x) + ", score= " + str(eq))
'''