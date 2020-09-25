import csv
import folium
from IPython.display import IFrame
from folium.plugins import HeatMap

f = open('경상남도 창원시_불법주정차단속정보_20200831_결과.csv', 'r')
rdr = csv.reader(f)

nodes = []

for line in rdr :
    if(line[6] == 'error') :
        continue
    
    lngIndex = line[7].index('lng')
    lat = line[7][8:lngIndex-3]
    lng = line[7][lngIndex+6:-1]
               
    geocode = [float(lat), float(lng)]
    nodes.append(geocode)
    #print(geocode)
    
m = folium.Map(location=(35.2279868, 128.6818143), zoom_start=13)

HeatMap(nodes,
        min_opacity=0.1,
        raduis=2,
        blur=30
       ).add_to(m)
       
m.save('heatMap.html')




