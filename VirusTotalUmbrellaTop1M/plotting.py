import csv
import matplotlib.pyplot as plt
import numpy as np
import statistics as stat


def plot_box(path_csv_vt, path_csv_full = None):
    with open(path_csv_vt) as csv_vt:
        reader_vt = csv.reader(csv_vt)
        dict_vt = dict(reader_vt)

        score_vt = list(dict_vt.values())
        array_score_vt = []
        for x in score_vt:
            array_score_vt.append(int(x))
        red_square = dict(markerfacecolor='r', marker='o')
        fig_box_vt, ax_box_vt = plt.subplots()
        ax_box_vt.set_title('Box VT')
        ax_box_vt.boxplot(array_score_vt, vert=False, flierprops=red_square)
        plt.savefig("/Volumes/PEPPE_DT/WorkspacePyCharm/VirusTotalUmbrellaTop1M/py_prova_merge/img_plot/box_vt.png")
        print(stat.mean(array_score_vt))
        print(stat.median(array_score_vt))
        print(stat.stdev(array_score_vt))
        print(stat.variance(array_score_vt))
        plt.show()


'''
 show the growth of domain scanned and scored by vt
'''
def plot_line_full(path_csv_100_full, path_csv_500_full, path_csv_1m_full):
    with open(path_csv_100_full) as full_100, open(path_csv_500_full) as full_500, open(path_csv_1m_full) as full_1:
        freader_100 = csv.reader(full_100)
        freader_500 = csv.reader(full_500)
        freader_1 = csv.reader(full_1)
        fdict_100 = dict(freader_100)
        fdict_500 = dict(freader_500)
        fdict_1 = dict(freader_1)
        print(len(fdict_100))
        print(len(fdict_500))
        print(len(fdict_1))
        len_value = [len(fdict_100), len(fdict_500), len(fdict_1)]
        label_x = ["100k", "500k", "1m"]
        diff_value = [100000 - len(fdict_100), 500000 - len(fdict_500), 1000000000 - len(fdict_1)]
        print("diff value")
        for x in diff_value:
            print(x)
        plt.plot(label_x, len_value, label = "vt")
        plt.plot(label_x, diff_value, label = "no_vt")
        plt.yscale("log")
        plt.suptitle("vtdetect_diff_nodetect")
        plt.legend()
        plt.savefig("/Volumes/PEPPE_DT/WorkspacePyCharm/VirusTotalUmbrellaTop1M/py_prova_merge/img_plot/line_full_det_diff.png")
        plt.show()


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
    with open(path_csv_vt) as csv_vt, open(path_csv_full) as csv_full:
        reader_vt = csv.reader(csv_vt)
        reader_full = csv.reader(csv_full)
        dict_vt = dict(reader_vt)
        dict_full = dict(reader_full)

        # domain_names_vt = dict_100k_vt.keys()
        score_vt = list(dict_vt.values())
        array_score_vt = []
        for x in score_vt:
            array_score_vt.append(int(x))


        # domain_names_full = dict_100k_full.keys()
        score_full = list(dict_full.values())
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

        plt.bar(r_vt, score_occurrence_dict_vt.values(), width, label="vt_tranco", log = True)
        plt.bar(r_full, score_occurrence_dict_full.values(), width, label="full")

        plt.xticks([r + width for r in range(len(labels))], labels)
        plt.yscale("log")
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

def box_plot_domain_names_len(csv_domain_names_len):
    """

    path = csv_domain_names_len.split("/")
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

    """
    with open(csv_domain_names_len) as csv_len:
        reader_csv = csv.reader(csv_len)
        array_len = list(reader_csv)
        array_int = []
        for x in array_len:
            print(type(x[0]))
            print(x[0])
            array_int.append(int(x[0]))
        plt.boxplot(array_int)
        plt.suptitle("boxplot domain names lenght")
        plt.savefig("/Volumes/PEPPE_DT/WorkspacePyCharm/VirusTotalUmbrellaTop1M/py_prova_merge/img_plot/boxplt_domain_names_lengt.png")
        plt.show()


if __name__ == "__main__":
    csv_100k_vt_path = "/Volumes/PEPPE_DT/WorkspacePyCharm/VirusTotalUmbrellaTop1M/py_prova_merge/100K_vt.csv"
    csv_100k_full_path = "/Volumes/PEPPE_DT/WorkspacePyCharm/VirusTotalUmbrellaTop1M/py_prova_merge/100K_full.csv"
    csv_1m_vt_path = "/Volumes/PEPPE_DT/WorkspacePyCharm/VirusTotalUmbrellaTop1M/py_prova_merge/1m_vt.csv"
    csv_1m_full_path = "/Volumes/PEPPE_DT/WorkspacePyCharm/VirusTotalUmbrellaTop1M/py_prova_merge/1m_full.csv"
    csv_500k_full_path = "/Volumes/PEPPE_DT/WorkspacePyCharm/VirusTotalUmbrellaTop1M/py_prova_merge/500K_full.csv"
    csv_500k_vt_path = "/Volumes/PEPPE_DT/WorkspacePyCharm/VirusTotalUmbrellaTop1M/py_prova_merge/500K_vt.csv"
    csv_domain_len_path = "/Volumes/PEPPE_DT/WorkspacePyCharm/VirusTotalUmbrellaTop1M/domain_names_len_1m.csv"

   # plot_bar(csv_100k_vt_path, csv_100k_full_path)
   # plot_bar(csv_1m_vt_path, csv_1m_full_path)
   # plot_bar(csv_500k_vt_path, csv_500k_full_path)

   # plot_box(csv_100k_vt_path)
   # plot_line_full(csv_100k_full_path, csv_500k_full_path, csv_1m_full_path)

    box_plot_domain_names_len(csv_domain_len_path)
