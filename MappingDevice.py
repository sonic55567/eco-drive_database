
from math import *
import json
from jmespath import search

def Distance(lat1,lng1,lat2,lng2):
    radlat1=radians(lat1)  
    radlat2=radians(lat2)  
    a=radlat1-radlat2  
    b=radians(lng1)-radians(lng2)  
    s=2*asin(sqrt(pow(sin(a/2),2)+cos(radlat1)*cos(radlat2)*pow(sin(b/2),2)))  
    earth_radius=6378.137  
    s=s*earth_radius  
    if s<0:  
        return -s  
    else:  
        return s

data = open("node_v6.json","rb").read()
data_node = json.loads(data)

data = open("node_index.json","rb").read()
data_index = json.loads(data)

data = open("converted.json","rb").read()
data_device = json.loads(data)

Lat_A=22.991715; Lng_A=120.222467 # 南京
Lat_B=22.9920653; Lng_B=120.2215513 # 北京
distance=Distance(Lat_A,Lng_A,Lat_B,Lng_B)
print(distance)

count = 0



"""
f = open("node_v7.json","w+",encoding="utf-8")
f.write(json.dumps(data_node, ensure_ascii=False, indent=1)) 
f.close()
"""


