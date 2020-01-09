import csv
import matplotlib.pyplot as plt
import numpy as np
import os


def plot_bar(path_csv_vt, path_csv_full):

    path = path_csv_full.split("/")
    type_file = path[-1]
    dim = 0
    if "1m_full" in type_file:
        dim = 100000000
    elif "500K" in type_file:
        dim = 500000
    elif "100K" in type_file:
        dim = 100000
    else:
        print("check the name of file")


    with open(path_csv_vt) as csv_100k_vt, open(path_csv_full) as csv_100k_full:
        reader_vt = csv.reader(csv_100k_vt)
        reader_full = csv.reader(csv_100k_full)
        dict_100k_vt = dict(reader_vt)
        dict_100k_full = dict(reader_full)

        # domain_names_vt = dict_100k_vt.keys()
        score_vt = list(dict_100k_vt.values())
        array_score_vt = []
        for x in score_vt:
            array_score_vt.append(int(x))


        # domain_names_full = dict_100k_full.keys()
        score_full = list(dict_100k_full.values())
        array_score_full = []
        for z in score_full:
            array_score_full.append(int(z))

        maximum_vt = max(array_score_vt)
        score_occurrence_dict_vt = {}
        for x in range(1, maximum_vt+1):
            score_occurrence_vt = sum(z == x for z in array_score_vt)
            print(""+str(x)+","+str(score_occurrence_vt))
            score_occurrence_dict_vt[str(x)] = score_occurrence_vt

        maximum_full = max(array_score_full)
        score_occurrence_dict_full = {}
        for y in range(1, maximum_full + 1):
            score_occurrence_full = sum(z == y for z in array_score_full)
            score_occurrence_dict_full[str(y)] = score_occurrence_full

        if maximum_vt == maximum_full:
            labels = []
            for x in range(1, int(maximum_full) + 1):
                labels.append(x)
        else:
            print("different label values")
            print(maximum_vt)
            print(maximum_full)
            lendif = maximum_full - maximum_vt
            last_score_occ = list(score_occurrence_dict_vt.keys())
            last = int(last_score_occ[-1])
            for x in range(1, lendif + 1):
                score_occurrence_dict_vt[str(last+x)] = 0
            print(len(score_occurrence_dict_vt))
            print(len(score_occurrence_dict_full))
            labels = []
            for x in range(1, int(maximum_full) + 1):
                print("labels")
                print(x)
                labels.append(x)

        print("dict full")
        for x,y in score_occurrence_dict_full.items():
            print(x,y)
        print("dict vt")
        for x,y in score_occurrence_dict_vt.items():
            print(x,y)

        width = 0.3
        r_vt = np.arange(len(labels))
        r_full = [x + width for x in r_vt]

        plt.bar(r_vt, score_occurrence_dict_vt.values(), width, label="vt_tranco")
        plt.bar(r_full, score_occurrence_dict_full.values(), width, label="full")

        plt.xticks([r + width for r in range(len(labels))], labels)
        plt.legend()

        if dim <= 100000:
            plt.suptitle("bar 100k")
            plt.savefig("/Volumes/PEPPE_DT/WorkspacePyCharm/VirusTotalUmbrellaTop1M/py_prova_merge/img_plot/bar_plot_100k.png")
        elif dim <= 500000:
            plt.suptitle("bar 500k")
            plt.savefig("/Volumes/PEPPE_DT/WorkspacePyCharm/VirusTotalUmbrellaTop1M/py_prova_merge/img_plot/bar_plot_500k.png")
        elif dim > 500000:
            plt.suptitle("bar 1m")
            plt.savefig("/Volumes/PEPPE_DT/WorkspacePyCharm/VirusTotalUmbrellaTop1M/py_prova_merge/img_plot/bar_plot_1m.png")
        else:
            print("wtf!")
        print("lunghezza")
        print(str(len(array_score_full)))
        print(dim)
        plt.show()


if __name__ == "__main__":
    csv_100k_vt_path = "/Volumes/PEPPE_DT/WorkspacePyCharm/VirusTotalUmbrellaTop1M/py_prova_merge/100K_vt.csv"
    csv_100k_full_path = "/Volumes/PEPPE_DT/WorkspacePyCharm/VirusTotalUmbrellaTop1M/py_prova_merge/100K_full.csv"
    csv_1m_vt_path = "/Volumes/PEPPE_DT/WorkspacePyCharm/VirusTotalUmbrellaTop1M/py_prova_merge/1m_vt.csv"
    csv_1m_full_path = "/Volumes/PEPPE_DT/WorkspacePyCharm/VirusTotalUmbrellaTop1M/py_prova_merge/1m_full.csv"
    csv_500k_full_path = "/Volumes/PEPPE_DT/WorkspacePyCharm/VirusTotalUmbrellaTop1M/py_prova_merge/500K_full.csv"
    csv_500k_vt_path = "/Volumes/PEPPE_DT/WorkspacePyCharm/VirusTotalUmbrellaTop1M/py_prova_merge/500K_vt.csv"
    plot_bar(csv_100k_vt_path, csv_100k_full_path)
    plot_bar(csv_1m_vt_path, csv_1m_full_path)
    plot_bar(csv_500k_vt_path, csv_500k_full_path)


