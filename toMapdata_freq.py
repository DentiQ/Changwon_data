import csv
import json
import os

os.chdir('C:/Users/Dongsun/OneDrive - 서울시립대학교/2020 2학기/창원 데이터')
f = open('경상남도 창원시_불법주정차단속정보_20200831_결과.csv', 'r')
rdr = csv.reader(f)

newlines = [] 
myline = [] # 주소, 위도-경도, 빈도
freq = []

for line in rdr:
    if(line[6] != 'error') :
        latIndex = line[7].index('lat')
        lngIndex = line[7].index('lng')
        lat = line[7][latIndex+6:lngIndex-3]
        lng = line[7][lngIndex+6:-1]
        location = [lat, lng]

        myline = [line[6], location]

        if(myline in newlines) :
            freq[newlines.index(myline)] += 1
        else :
            newlines.append(myline)
            freq.append(1)
f.close

index = 0
for newline in newlines:
    newline.append(freq[index])
    newlines[index] = newline
    index+=1
    
f = open('지도 데이터 빈도.csv', 'w', newline='')
wr = csv.writer(f)
wr.writerows(newlines)
f.close
        

