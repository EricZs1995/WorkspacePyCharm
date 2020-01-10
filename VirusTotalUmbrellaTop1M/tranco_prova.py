import time
from datetime import  datetime
import json
import csv

all_filter_json = "/Volumes/PEPPE_DT/WorkspacePyCharm/VirusTotalUmbrellaTop1M/py_prova_merge/prova_merge/all_filter.json"
tranco_csv = "/Volumes/PEPPE_DT/WorkspacePyCharm/VirusTotalUmbrellaTop1M/py_prova_merge/tranco-top-1m.csv"

with open(all_filter_json) as file:
    json_data = json.load(file)

print(type(json_data))

'''
list of domain name scanned (key values of dict 'json_data')
'''

index = []
for a in json_data.items():
    index.append(a[0])

'''
for x in index:
    print(x)
'''


'''
for x in index:
    for p in json_data[x]:
        print("domain: " + str(x) + ", score: " + str(p['score']))
'''

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
for x in index:
    for p in json_data[x]:
        if p['score'] > 0:
            print(x)
            for dom in tranco_domain:
                if dom == x:
                    fp_dict[x] = p['score']
                    score_l.append(p['score'])
end = datetime.now()
for x,y in fp_dict.items():
    print(x, y)

print('Duration: {}'.format(end - start))
print(len(index))
print(len(fp_dict))
perc = (len(fp_dict)/len(index))
print("% :" + str(perc))
maximum = max(score_l)
print("Max score: " + str(maximum))


for x in range(1,maximum+1):
    eq = sum(num == x for num in score_l)
    print("Num of score equal to " + str(x) + " is :" + str(eq))

