
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

Lat_A=22.9920653; Lng_A=120.2215513 # 南京
Lat_B=22.9871641; Lng_B=120.2228994 # 北京
distance=Distance(Lat_A,Lng_A,Lat_B,Lng_B)
print(distance)

count = 0

device_lat = data_device["Device"]["S014401"]["Longitude"]
device_lon = data_device["Device"]["S014401"]["Latitude"]
node_lat = data_node["1650294487"]["lat"]
node_lon = data_node["1650294487"]["lon"]

print(node_lat)
print(node_lon)
print(device_lat)
print(device_lon)
print(Distance(device_lat, device_lon, node_lat, node_lon))


for i in data_device["Device"] :
    device_lat = data_device["Device"][str(i)]["Longitude"]
    device_lon = data_device["Device"][str(i)]["Latitude"]
    for j in data_node :
        if data_node[str(j)]["intersection"] == True :
            if Distance(device_lat, device_lon, data_node[str(j)]["lat"], data_node[str(j)]["lon"]) <= 0.05 :
                if "DeviceID" not in data_node[str(j)].keys() :
                    data_node[str(j)]["DeviceID"] = str(i)
                    print("add")
                    count = count+1
print(count)


f = open("node_v7.json","w+",encoding="utf-8")
f.write(json.dumps(data_node, ensure_ascii=False, indent=1)) 
f.close()


