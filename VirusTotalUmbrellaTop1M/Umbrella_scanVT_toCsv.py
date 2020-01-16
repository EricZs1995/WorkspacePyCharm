import csv
import json
import os
from datetime import datetime
import requests
import sys
import time


def run():
    path_csv_20 = sys.argv[1]
    api_key_in = sys.argv[2]
    url = 'https://www.virustotal.com/vtapi/v2/url/report'

    dirName = os.path.basename(path_csv_20)
    file_basename = str(dirName.split("/")[-1].split(".")[0])

    '''
    full_name_csv = basename[-1].split()
    base_name_csv_l = full_name_csv.split('.')
    base_name_csv = base_name_csv_l[0]
    '''

    with open(path_csv_20, 'r') as csv_umb20:
        reader_csv = csv.reader(csv_umb20, delimiter=',')
        list_dom = list(reader_csv)

    list_domain_names = []
    lung_list = len(list_dom)

    for i in range(0,lung_list):
        list_domain_names.append(list_dom[i][0])


    scanner_dict = {
            'CLEANMX':0,
            'DNS8':1,
            'VXVAULT':2,
            'ZDBZEUS':3,
            'TENCENT':4,
            'MALWAREPATROL':4,
            'ZCLOUDSEC':5,
            'COMODOVALKYRIEVERDICT':6,
            'PHISHLABS':7,
            'K7ANTIVIRUS':8,
            'FRAUDSENSE':9,
            'VIRUSDIEEXTERNALSITESCAN':10,
            'SPAMHAUS':11,
            'QUTTERA':12,
            'AEGISLABWEBGUARD':13,
            'MALWAREDOMAINLIST':14,
            'ZEUSTRACKER':15,
            'ZVELO':17,
            'GOOGLESAFEBROWSING':18,
            'KASPERSKY':19,
            'BITDEFENDER':20,
            'DR.WEB':21,
            'G-DATA':22,
            'SEGASEC':23,
            'CYBERCRIME':24,
            'MALWAREDOMAINBLOCKLIST':25,
            'CRDF':26,
            'TRUSTWAVE':27,
            'WEBSECURITYGUARD':28,
            'CYRADAR':29,
            'DESENMASCARA.ME':30,
            'ADMINUSLABS':31,
            'MALWAREBYTESHPHOSTS':32,
            'OPERA':33,
            'ALIENVAULT':35,
            'EMSISOFT':36,
            'MALC0DEDATABASE':37,
            'MALWARES.COMURLCHECKER':38,
            'PHISHTANK':39,
            'EONSCOPE':40,
            'MALWARED':41,
            'AVIRA':42,
            'NOTMINING':43,
            'OPENPHISH':44,
            'ANTIY-AVL':45,
            'FORCEPOINTTHREATSEEKER':46,
            'SCUMWARE.ORG':47,
            'ESTSECURITY-THREATINSIDE':48,
            'COMODOSITEINSPECTOR':49,
            'YANDEXSAFEBROWSING':50,
            'MALEKAL':51,
            'ESET':52,
            'SOPHOS':53,
            'URLHAUS':54,
            'SECUREBRAIN':55,
            'NUCLEON':56,
            'BADWARE.INFO':57,
            'SUCURISITECHECK':58,
            'BLUELIV':59,
            'NETCRAFT':60,
            'AUTOSHUN':61,
            'THREATHIVE':62,
            'FRAUDSCORE':63,
            'QUICKHEAL':64,
            'RISING':65,
            'URLQUERY':66,
            'STOPBADWARE':67,
            'FORTINET':68,
            'ZEROCERT':69,
            'SPAM404':70,
            'SECUROLYTICS':71,
            'BAIDU-INTERNATIONAL':72,
            'ZEROFOX':73,
            'CERTLY':74,
            'C-SIRT':75,
            'WEBSENSETHREATSEEKER':76,
            'WEBUTATION':77,
            'PARETOLOGIC':78,
            'WEPAWET':79,
            'SPYEYETRACKER':80,
            'CLOUDSTAT':81,
            'PALEVOTRACKER':82,
            'WOT':83,
            'TRENDMICRO':84,
            'BOTVRIJ.EU':85,
            'SANGFOR':86,
            'VIRUSDIE':87,
            'MINOTAUR':88,
            'PREBYTES':89
        }

    fieldsnames = ['domain name','response_code','positives','scandate','total']
    scanners_dict_keys = scanner_dict.keys()
    for x in scanners_dict_keys:
        fieldsnames.append(str(x))

    fields_to_write = []
    count = 0
    with open('/Volumes/PEPPE_DT/WorkspacePyCharm/VirusTotalUmbrellaTop1M/Umbrella_scanVT_V2/' + file_basename + '.csv', mode='a') as csv_out:
        writer_csv = csv.writer(csv_out, delimiter=',')
        writer_csv.writerow(fieldsnames)
        for domain_name in list_domain_names:
            count += 1
           # time.sleep(15)
            params_d = {'apikey': api_key_in, 'resource': domain_name}
            response = requests.get(url, params=params_d)
            code = response.status_code
            json_response = response.json()
            if code == 200 and json_response['response_code'] != 0:
                print(count)

                fields_to_write.append(json_response['resource'])
                fields_to_write.append(str(json_response['response_code']))
                fields_to_write.append(str(json_response['positives']))
                fields_to_write.append(str(json_response['scan_date']))
                fields_to_write.append(str(json_response['total']))
                json_keys = []
                json_keys_mod = {}
                for x in json_response['scans'].keys():
                    json_keys.append(str(x))
                  #  print(x)
                for x in json_keys:
                    z = x.strip()
                    z = z.replace(" ","")
                    z = z.upper()
                   # print("chiave: " + z + " valore :" + x)
                    #json_keys_mod.append(str(x))
                    json_keys_mod[str(z)] = str(x)
                for scanners_key in scanners_dict_keys:
                    if scanners_key in json_keys_mod.keys():
                        scan_part = json_response['scans'][json_keys_mod[str(scanners_key)]]
                        txt_scan = scan_part['result']
                        fields_to_write.append(txt_scan)
                    else:
                        fields_to_write.append('null')
                writer_csv.writerow(fields_to_write)
                fields_to_write = []
                json_keys = []
                json_keys_mod = {}
            elif json_response['response_code'] == 0:
                print(str(count) + " , response code 0")
                fields_to_write.append(json_response['resource'])
                fields_to_write.append(str(json_response['response_code']))
                #positives
                fields_to_write.append('null')
                #scandate
                fields_to_write.append('null')
                #total
                fields_to_write.append('null')
                for x in scanners_dict_keys:
                    fields_to_write.append('null')
                writer_csv.writerow(fields_to_write)
                fields_to_write = []
            else:
                print ("new problem")
           # if count == 2:
            #    break
            time.sleep(0.07)


if __name__ == "__main__":
    start = datetime.now()
    run()
    end = datetime.now()

    print('Duration: {}'.format(end - start))