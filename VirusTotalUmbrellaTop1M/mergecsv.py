import glob
import csv

path_folder = "/Volumes/PEPPE_DT/WorkspacePyCharm/VirusTotalUmbrellaTop1M/prova_merge_csv"
path_csv_out = "/Volumes/PEPPE_DT/WorkspacePyCharm/VirusTotalUmbrellaTop1M/csv_merge_prova_out.csv"
csv_restrict_out = "/Volumes/PEPPE_DT/WorkspacePyCharm/VirusTotalUmbrellaTop1M/restrict_out.csv"
delimiter = ','
count_first = 0
list_files = sorted(glob.glob(path_folder + '/x*.csv'))
count_file = 0
with open(path_csv_out, mode='a') as csv_out, open(csv_restrict_out, mode='a') as csv_r_out:
    writer_out = csv.writer(csv_out)
    writer_out2 = csv.writer(csv_r_out)
    for x in list_files:
        count_file += 1
        print(count_file)
        if count_first == 0:
            with open(x, mode='r') as csv_in:
                reader = csv.reader(csv_in, delimiter=delimiter)
                for row in reader:

                    writer_out.writerow(row)

                    writer_out2.writerow(row)
                count_first = 1
        else:
            with open(x, mode='r') as csv_in:
                reader = csv.reader(csv_in, delimiter=delimiter)
                count_row = 0
                for row in reader:
                    if count_row == 0:
                        count_row = 1
                        continue
                    else:
                        writer_out.writerow(row)

                        writer_out2.writerow(row)
       # if count_file == 1:
          #  break