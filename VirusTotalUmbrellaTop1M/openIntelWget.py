import wget 
import sys 
from datetime import datetime,timedelta

date1 = sys.argv[1]
date2 = sys.argv[2]
date_format = '%d/%m/%Y'

date_start = datetime.strptime(date1, date_format)
date_end = datetime.strptime(date2, date_format)

#print(date_start.month)

period = (date_end - date_start).days
print(period)

#print(date_start + timedelta(days=30))
# range (1,3) = 1,2


for i in range(0, period + 1):
    new_base = date_start + timedelta(days=i)
    print(str(new_base)+ "\n")
    if(new_base.day<10):
        file_date = str(new_base.year) + str(new_base.month) +"0"+str(new_base.day)
    else:
        file_date =str(new_base.year)+str(new_base.month)+str(new_base.day)
    print(file_date)
    file = wget.download("https://data.openintel.nl/data/open-tld/2019/openintel-open-tld-"+file_date+".tar",
                         out="./openintel/"+file_date+".tar")



