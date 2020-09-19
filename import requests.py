import requests
import csv
import json
import os

os.chdir('C:/Users/Dongsun/OneDrive - 서울시립대학교/2020 2학기/창원 데이터')
f = open('경상남도 창원시_불법주정차단속정보_20200831.csv', 'r')
rdr = csv.reader(f)
index = 0
lines = []
for line in rdr:
    index+=1
    if index > 1 :
        if(line[3] != 'CCTV') :
            place = line[2]
            url = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=' + place +'&inputtype=textquery&fields=geometry,formatted_address&locationbias=circle:20000@35.2275496,128.6810085&key=AIzaSyDXwvMn4rRZ7e8yKR-gykRiO6dYQPJpOmU'
            response = requests.get(url)
            json_response = json.loads(response.text)
            if (json_response['status'] == 'OK') :
                line.append(json_response['candidates'][0]['formatted_address'])
                line.append(json_response['candidates'][0]['geometry']['location'])
                print('Success with line %d!' %(index))
            else :
                line.append('error')
        lines.append(line)
    if index > 10000 :
        break
f.close

nf = open('경상남도 창원시_불법주정차단속정보_20200831_결과.csv', 'w', newline='')
wr = csv.writer(nf)
wr.writerows(lines)
nf.close
