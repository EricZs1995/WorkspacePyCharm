import csv
import json


def calc_score_occ(csv_full_path):
    with open(csv_full_path) as csv_path:
        csv_read = csv.reader(csv_path)
        dict_csv = dict(csv_read)

        value_score = list(dict_csv.values())
        score_array = []
        for x in value_score:
            score_array.append(int(x[0]))
          #  print(int(x[0]))

        print("lunghezza")
        print(len(score_array))
        max_val = max(score_array)
        print("max")
        print(max_val)
        for x in range(1,max_val + 1):
            eq = sum(val == x for val in score_array)
            print("Valore : " + str(x) + ", occorrenza: " + str(eq))

def calc_score_json(json_path):
    with open(json_path) as file_json:
        json_data = json.load(file_json)

    '''
    list of domain name scanned (key values of dict 'json_data')
    '''
    index = []
    for a in json_data.items():
        index.append(a[0])

    all_score_not_null = {}
    for x in index:
        for p in json_data[x]:
            if p['score'] > 0:
                    # dict : domain with score not null
                 all_score_not_null[x] = p['score']

    value_json_score = list(all_score_not_null.values())
    array_json_score = []
    for x in value_json_score:
        array_json_score.append(int(x))

    json_max = max(array_json_score)
    print("json max")
    print(json_max)
    for x in range(1,json_max+1):
        eq = sum(val == x for val in array_json_score)
        print("Valore : " + str(x) + ", occorrenza: " + str(eq))




if __name__ == "__main__":
    path_100_csv = "/Volumes/PEPPE_DT/WorkspacePyCharm/VirusTotalUmbrellaTop1M/py_prova_merge/100K_full.csv"
    path_500_csv = "/Volumes/PEPPE_DT/WorkspacePyCharm/VirusTotalUmbrellaTop1M/py_prova_merge/500K_full.csv"
    path_1_csv = "/Volumes/PEPPE_DT/WorkspacePyCharm/VirusTotalUmbrellaTop1M/py_prova_merge/1m_full.csv"
    path_500_json = "/Volumes/PEPPE_DT/WorkspacePyCharm/VirusTotalUmbrellaTop1M/merge_py_500k/all_filter.json"
    path_1_json = "/Volumes/PEPPE_DT/WorkspacePyCharm/VirusTotalUmbrellaTop1M/merge_py_1m/all_filter.json"
    path_100_json = "/Volumes/PEPPE_DT/WorkspacePyCharm/VirusTotalUmbrellaTop1M/merge_py_100k/all_filter.json"
    calc_score_occ(path_100_csv)
    calc_score_json(path_100_json)