import csv
import requests
import json
import time
import sys
import os
from datetime import datetime

#path del file csv da passare da cli
path = sys.argv[1]
api_k = sys.argv[2]



#path ="/Volumes/PEPPE_DT/UmbrellaTop1M/top-1m.csv"
#path = "/Volumes/PEPPE_DT/umbrellasplit/xaa.csv"
url = 'https://www.virustotal.com/vtapi/v2/url/report'
dirName = os.path.basename(path)
basename = dirName.split("/")
name_json = basename[-1]


#crazione di lista di lista
with open(path,'r') as csvF:
    csv_reader= csv.reader(csvF,delimiter=',')
    list_domain = list(csv_reader)
    
#print(len(list_domain))


'''
params = {'apikey': api_k, 'resource':list_domain[0][1]}
response = requests.get(url, params=params)
print(type(response))
#print(json.dumps(response , indent=4))
json_response = response.json()
json_print= json.dumps(json_response, indent=4)
print(json_print)
print( "Dominio:" + json_response["resource"] + ", Positivies:" + str(json_response["positives"]))
'''


file_w1 = open(name_json + "_filter.json" , "w+")
file_w2 = open(name_json + "_204_error.json" , "w+")


l=len(list_domain)
#l = 10
r = range(0,l)

#print(r)
#print("{")
file_w1.write("{")
file_w2.write("{")
count_rc0 = 0
start = datetime.now()
for i in r:
    time.sleep(15)
    print(i)
    params_d = {'apikey' : api_k,'resource' : list_domain[i]}
    response = requests.get(url,params=params_d)
    code=response.status_code
    print(response.status_code)
    '''
    if(response.status_code == 204):
        time.sleep(20)
    
    response_n = requests.get(url,params=params_d)
    code_n=response.status_code
    print(response_n.status_code)
    
    
    while(response.status_code == 204):
        response = requests.get(url,params=params_d)
    '''
    json_response = response.json()
    print(str(json_response["response_code"]))
    #agg controllo if(positives!=0)->stampa

    
   # print("N: " + str(i + 1) + "- Dominio: " + json_response["resource"] + ", Total: " + str(json_response["total"]) + ", Positives: " + str(json_response["positives"]))
    if(code==204):
        par = "}"
        #print("}")
        file_w1.write(par)
        file_w2.write(par)
        file_w1.close()
        file_w2.close()
        exit()
    elif(code == 200 and json_response["response_code"] != 0):
        if(i != (l-1)):
            file_w1.write("\"" +json_response["resource"]+ "\" : [{ " +
              "\"score\" :" + str(json_response["positives"]) + "," +
              "\"status response\" :" + str(code)+ "," +
              "\"total\" :" + str(json_response["total"]) +
              "}], \n")
        else:
            file_w1.write("\"" +json_response["resource"]+ "\" : [{ " +
              "\"score\" :" + str(json_response["positives"]) + "," + 
              "\"status response\" :" + str(code)+ "," + 
              "\"total\" :" + str(json_response["total"])+
              "}] } \n")
            file_w2.write("}")
            file_w1.close()
            file_w2.close()

            #print("}")
    elif (json_response["response_code"] == 0):
            if (count_rc0 == 0):
                count_rc0 += 1
                file_w2.write("\"" + json_response["resource"] + "\" : [{ " +
                              "\"score\" :" + str(0) + "," +
                              "\"status response\" :" + str(code) + "," +
                              "\"total\" :" + str(0) +
                              "}] \n")
            elif (count_rc0 == 0 and i == l):
                file_w2.write("\"" + json_response["resource"] + "\" : [{ " +
                              "\"score\" :" + str(0) + "," +
                              "\"status response\" :" + str(code) + "," +
                              "\"total\" :" + str(0) +
                              "}] } \n")
                file_w1.write("}")
                file_w1.close()
                file_w2.close()
            elif (i != (l - 1)):
                file_w2.write(",\"" + json_response["resource"] + "\" : [{ " +
                              "\"score\" :" + str(0) + "," +
                              "\"status response\" :" + str(code) + "," +
                              "\"total\" :" + str(0) +
                              "}] \n")
            else:
                file_w2.write(",\"" + json_response["resource"] + "\" : [{ " +
                              "\"score\" :" + str(0) + "," +
                              "\"status response\" :" + str(code) + "," +
                              "\"total\" :" + str(0) +
                              "}] } \n")
                file_w1.write("}")
                file_w1.close()
                file_w2.close()
                # print("}")
    else:
        file_w1.write("} \n")
        file_w2.write("} \n")
        #print("}")
        #print(code)
        file_w1.close()
        file_w2.close()
        exit()
        
end = datetime.now()

print('Duration: {}'.format(end - start))
#print("}")




