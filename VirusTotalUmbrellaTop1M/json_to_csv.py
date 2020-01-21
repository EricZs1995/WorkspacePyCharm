import csv
import json
import os
import glob
from datetime import  datetime

def json_csv ():
    path_terrore = "/Volumes/PEPPE_DT/WorkspacePyCharm/VirusTotalUmbrellaTop1M/all_info"
    path_nomi = "/Volumes/PEPPE_DT/WorkspacePyCharm/VirusTotalUmbrellaTop1M/nomi_scan_vt.txt"


    list_files = []
    for file in glob.glob(path_terrore + "/*json"):
        list_files.append(file)

    '''
    with open(list_files[0]) as json_0:
        read_j = json.load(json_0)
       # print(read_j)
        print(type(read_j))
        print(read_j['scans'])
        print(type(read_j['scans']))
        print(read_j['scans'].keys())
        print(read_j['scans']['CLEAN MX']['result'])
        scanpart = read_j['scans']['CLEAN MX']
        print(scanpart['result'])
    
    
    '''




    scanner_dict = {
        'CLEAN MX':0,
        'DNS 8':1,
        'VX Vault':2,
        'ZDB Zeus':3,
        'Tencent':4,
        'MalwarePatrol':4,
        'ZCloudsec':5,
        'Comodo Valkyrie Verdict':6,
        'PhishLabs':7,
        'K7AntiVirus':8,
        'FraudSense':9,
        'Virusdie External Site Scan':10,
        'Spamhaus':11,
        'Quttera':12,
        'AegisLab WebGuard':13,
        'MalwareDomainList':14,
        'ZeusTracker':15,
        'zvelo':17,
        'Google Safebrowsing':18,
        'Kaspersky':19,
        'BitDefender':20,
        'Dr.Web':21,
        'G-Data':22,
        'Segasec':23,
        'CyberCrime':24,
        'Malware Domain Blocklist':25,
        'CRDF':26,
        'Trustwave':27,
        'Web Security Guard':28,
        'CyRadar':29,
        'desenmascara.me':30,
        'ADMINUSLabs':31,
        'Malwarebytes hpHosts':32,
        'Opera':33,
        'AlienVault':35,
        'Emsisoft':36,
        'Malc0de Database':37,
        'malwares.com URL checker':38,
        'Phishtank':39,
        'EonScope':40,
        'Malwared':41,
        'Avira':42,
        'NotMining':43,
        'OpenPhish':44,
        'Antiy-AVL':45,
        'Forcepoint ThreatSeeker':46,
        'SCUMWARE.org':47,
        'ESTsecurity-Threat Inside':48,
        'Comodo Site Inspector':49,
        'Yandex Safebrowsing':50,
        'Malekal':51,
        'ESET':52,
        'Sophos':53,
        'URLhaus':54,
        'SecureBrain':55,
        'Nucleon':56,
        'BADWARE.INFO':57,
        'Sucuri SiteCheck':58,
        'BlueLiv':59,
        'Netcraft':60,
        'AutoShun':61,
        'ThreatHive':62,
        'FraudScore':63,
        'Quick Heal':64,
        'Rising':65,
        'URLQuery':66,
        'StopBadware':67,
        'Fortinet':68,
        'ZeroCERT':69,
        'Spam404':70,
        'securolytics':71,
        'Baidu-International':72,
        'Zerofox':73
    }

    fieldsnames = ['domain name','positives','scandate','total']

    scanners_dict_keys = scanner_dict.keys()
    list_of_scanners = []
    for x in scanners_dict_keys:
        fieldsnames.append(str(x))
        list_of_scanners.append(str(x))

    '''
    count = 0
    for x in fieldsnames:
        count +=1
        print(x)
    
    print(count)
    '''
    count = 0
    list_csv_towrite = []

    with open("info_scan_allVT_new.csv", mode='a') as csv_fileVT:
        writer_csv = csv.writer(csv_fileVT, delimiter=',')
        writer_csv.writerow(fieldsnames)
        for file_json in list_files:
            count += 1
            print(count)
            with open(file_json) as file:
                read_json = json.load(file)
                list_csv_towrite.append(read_json['resource'])
                list_csv_towrite.append(str(read_json['positives']))
                list_csv_towrite.append(str(read_json['scan_date']))
                list_csv_towrite.append(str(read_json['total']))
                for scanners_key in scanners_dict_keys:
                    if scanners_key in read_json['scans'].keys():
                        scan_part = read_json['scans'][scanners_key]
                        txt_scan = scan_part['result']
                        list_csv_towrite.append(txt_scan)
                    else:
                        list_csv_towrite.append('null')
                writer_csv.writerow(list_csv_towrite)
                list_csv_towrite = []
                for key in read_json['scans'].keys():
                    if key in scanners_dict_keys or key in list_of_scanners :
                        continue
                    else:
                        list_of_scanners.append(key)
          #  if count == 500:
           #     break
    for x in list_of_scanners:
        if x in scanners_dict_keys:
            continue
        else:
            print(x)



if __name__ == "__main__":
    start = datetime.now()
    json_csv()
    end = datetime.now()
    print("duration {}".format(end - start))

    # inserire scan date