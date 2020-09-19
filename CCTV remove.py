import requests
import csv
import json
import os

os.chdir('C:/Users/Dongsun/OneDrive - 서울시립대학교/2020 2학기/창원 데이터')
f = open('경상남도 창원시_불법주정차단속정보_20200831.csv', 'r')
rdr = csv.reader(f)
lines = []
for line in rdr:
    if(line[3] == 'CCTV') :
        continue
    lines.append(line)
    
f.close

nf = open('경상남도 창원시_불법주정차단속정보_20200831_수정.csv', 'w', newline='')
wr = csv.writer(nf)
wr.writerows(lines)
nf.close
