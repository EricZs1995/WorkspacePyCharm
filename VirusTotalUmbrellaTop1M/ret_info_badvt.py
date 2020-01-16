import  json
import requests
import  time
import sys
import csv
from jsonmerge import merge
from datetime import  datetime
import pprint
import os


"""

try to retrieve information about "scans" filed from the response send by VirusTotal

'scans':{
    'SCANNER_X': {
        'detected': false,
        'result': 'clean site'
    },
    'SCANNER_Y': {
        'detected': false,
        'result': 'clean site'
    }
}
"""


def scans_info_from_vt(path_save_json, path_csv_in,list_of_key):
    """
    :param path_save_json: path of json where save the output
    :param path_csv_in: "all_filter.json" in "merge_py_1m"
    :param list_of_key: list of api keys
    :return:
    """
    url = 'https://www.virustotal.com/vtapi/v2/url/report'
    count = 0
    index = 0
    leng = len(list_of_key)
    respones = []
    with open(path_csv_in) as csv_in, open(path_save_json, "+w") as json_out:
        reader_csv = csv.reader(csv_in)
        csv_dict = dict(reader_csv)
        list_domain_name = []
        for key,value in csv_dict.items():
            list_domain_name.append(str(key))
        json_out.write("[ \n")
        for domain in list_domain_name:
            if count <= 19999:
                index = 0
            elif 20000 <= count <= 39999:
                index = 1
            elif 40000 <= count <= 59999:
                index = 2
            elif 60000 <= count <= 79999:
                index = 3
            else:
                print("need more keys")
            time.sleep(0.08)
            params_d = {'apikey': list_of_key[index], 'resource': domain}
            response = requests.get(url, params=params_d)
            code = response.status_code
            if code == 200:
                    count += 1
                    print("count : " + str(count) + ", domain: " + domain)
                    json_response = json.dumps(response.json(), indent=4)
                   # print(json_response)
                   # print(type(json_response))
                    #respones.append(json_response)
                   # with open(path_save_json, "+w") as json_out:
                    if count == 75146:
                        json_out.write(json_response)
                        break
                    else:
                        json_out.write(json_response + ", \n")
            else:
                print(code)
                print("terminatocle")

        json_out.write("\n ]")


def scans_info_for_domain(path_csv,keys, path_all_info):
    url = 'https://www.virustotal.com/vtapi/v2/url/report'
    count = 0
    index = 0
    with open(path_csv) as csv_domain:
        read_csv = csv.reader(csv_domain)
        csv_dict = dict(read_csv)
        list_domain_name = []
        for key, value in csv_dict.items():
            list_domain_name.append(str(key))
        for domain in list_domain_name:
            if count <= 19999:
                index = 0
            elif 20000 <= count <= 39999:
                index = 1
            elif 40000 <= count <= 59999:
                index = 2
            elif 60000 <= count <= 79999:
                index = 3
            else:
                print("need more keys")
            time.sleep(0.07)
            params_d = {'apikey': keys[index], 'resource': domain}
            response = requests.get(url, params=params_d)
            code = response.status_code
            if code == 200:
                count += 1
                print("count : " + str(count) + ", domain: " + domain)
                json_response = response.json()
                domain_json = domain + ".json"
                with open(os.path.join(path_all_info, domain_json), "w") as json_dom:
                    json.dump(json_response, json_dom, indent=4)
            elif code == 204:
                print("richieste terminate")
            else:
                print("il codice è :" + str(code))





def all_info_toCSV(all_info_json_path, csv_out=None):
    with open(all_info_json_path, "rb") as json_path:
        reader_json = json.load(json_path)


    '''
    print("caricati")
    print(type(reader_json))
    
    json_items = []
    for item in reader_json.items():
        json_items.append(item)
    count = 0
    print(len(json_items))
    for x in json_items:
        count += 1
        print(x + "\n")
        if count == 3:
            break
    '''


if __name__ == "__main__":
    path_csv1M = "/Volumes/PEPPE_DT/WorkspacePyCharm/VirusTotalUmbrellaTop1M/py_prova_merge/1m_full.csv"
    save_path = "/Volumes/PEPPE_DT/WorkspacePyCharm/VirusTotalUmbrellaTop1M/merge_py_1m/all_info/all_info.json"
    all_info_fold = "/Volumes/PEPPE_DT/WorkspacePyCharm/VirusTotalUmbrellaTop1M/all_info"


    all_keys = str(sys.argv[1])
    keys_l = all_keys.split(",")
    path_csv_split = sys.argv[2]

    '''
    start = datetime.now()
    scans_info_from_vt(save_path, path_csv1M, keys)
    end = datetime.now()
    print('Duration: {}'.format(end - start))
    '''
   # all_info_toCSV(save_path)
    start = datetime.now()
    scans_info_for_domain(path_csv_split, keys_l, all_info_fold)
    end = datetime.now()
    print('Duration: {}'.format(end - start))