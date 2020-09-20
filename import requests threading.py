import requests
import csv
import json
import threading
import time
import os

os.chdir('C:/Users/Dongsun/OneDrive - 서울시립대학교/2020 2학기/창원 데이터')

def append_line(url, targetList, line):
    response = requests.get(url)
    json_response = json.loads(response.text)
    if(json_response['status'] == 'OK') :
        line.append(json_response['candidates'][0]['formatted_address'])
        line.append(json_response['candidates'][0]['geometry']['location'])
    else : 
        line.append('error')
    targetList.append(line)
    time.sleep(1)

f = open('경상남도 창원시_불법주정차단속정보_20200831_수정.csv', 'r')
rdr = csv.reader(f)
index = 0
lines = []
for line in rdr:
    index+=1
    if index > 1 :
        place = line[2]
        url = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=' + place +'&inputtype=textquery&fields=geometry,formatted_address&locationbias=circle:20000@35.2275496,128.6810085&key=YOUR_KEY_HEAR'
        t1 = threading.Thread(target=append_line, args=(url, lines, line))
        t1.start()
f.close
print('complete!')
nf = open('경상남도 창원시_불법주정차단속정보_20200831_결과.csv', 'w', newline='')
wr = csv.writer(nf)
wr.writerows(lines)
nf.close
t1.join()
