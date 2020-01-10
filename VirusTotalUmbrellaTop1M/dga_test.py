import  csv
import matplotlib.pyplot as plt
from datetime import datetime


def hasdig(word):
    return any(s.isdigit() for s in word)


def list_digitwithwords(path__csv):
    with open(path__csv) as csv_path:
        reader_csv = csv.reader(csv_path)
        dict_csv = dict(reader_csv)
        domain_names = list(dict_csv.keys())
        list_domainwithdig = []
        for names in domain_names:
            cond = hasdig(names)
            if cond:
                list_domainwithdig.append(names)

    for x in list_domainwithdig:
        print(x)

    print(len(list_domainwithdig))
    print("lunghezza")
    print(len(domain_names))


def domain_name_len(path__csv):
    with open(path__csv) as path_csv:
        reader_csv = csv.reader(path_csv)
        dict_csv = dict(reader_csv)
        domain_names = list(dict_csv.keys())
        leng_domain_names = []
        for x in domain_names:
            leng_domain_names.append(len(x))
            print(x + " " + str(len(x)))
        print("massimo")
        mass = max(leng_domain_names)
        print(max(leng_domain_names))
        count = 0
        for x in domain_names:
            if len(x) == mass:
                print("pos")
                print(count)
                print(x)
            count += 1
    try:
        with open("domain_names_len_1m.csv", "w", newline="") as out:
            writer_vt = csv.writer(out)
            for value in leng_domain_names:
                writer_vt.writerow([value])
    except IOError:
        print("I/O error write 'domain_names_len_1m")


if __name__ == "__main__":
    path_full_1m = "/Volumes/PEPPE_DT/WorkspacePyCharm/VirusTotalUmbrellaTop1M/py_prova_merge/1m_full.csv"
    path_full_100 = "/Volumes/PEPPE_DT/WorkspacePyCharm/VirusTotalUmbrellaTop1M/py_prova_merge/100K_full.csv"
    path_full_500 = "/Volumes/PEPPE_DT/WorkspacePyCharm/VirusTotalUmbrellaTop1M/py_prova_merge/500K_full.csv"
    path_vt_1m = "/Volumes/PEPPE_DT/WorkspacePyCharm/VirusTotalUmbrellaTop1M/py_prova_merge/1m_vt.csv"
    path_vt_100 = "/Volumes/PEPPE_DT/WorkspacePyCharm/VirusTotalUmbrellaTop1M/py_prova_merge/100K_vt.csv"
    path_vt_500 = "/Volumes/PEPPE_DT/WorkspacePyCharm/VirusTotalUmbrellaTop1M/py_prova_merge/500K_vt.csv"
   # list_digitwithwords(path_vt_1m)
    domain_name_len(path_full_100)