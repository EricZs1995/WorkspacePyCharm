import sys
import os
from datetime import datetime,timedelta
import csv


path = sys.argv[1]

with open(path, 'r') as csvF:
    csv_reader = csv.reader(csvF, delimiter=',')
    list_domain = list(csv_reader)

l = len(list_domain)
r = range(0, l)
i=0


for j in r:
    if ( list_domain[j] == " "):
        break
    print("i:" + str(i) + ", nome dominio :" + str(list_domain[j]) + " tipo 0:" + str(type(list_domain[j])))
    i += 1


