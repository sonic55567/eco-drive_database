import math
import json
from jmespath import search
from math import *

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

data = open("result_named_node_v3.json","rb").read()
data_node_v3 = json.loads(data)

data = open("result.json","rb").read()
data_way = json.loads(data)

data = open("converted.json","rb").read()
data_trafficSignal = json.loads(data)

# find the closest node
min = 10000
index = -1
notMap = 0
x = 0
y = 0
for i in data_trafficSignal["Device"].items():
    x = i[1]["Longitude"]
    y = i[1]["Latitude"]
    print("(", x, ",", y, ")")
    a = []
    b = []
    minIndex = -1
    min = 0.15
    for j in range(len(data_node_v3)) :
        node_x = data_node_v3[j]["lat"]
        node_y = data_node_v3[j]["lon"]
        dist = Distance(x, y, node_x, node_y)
        if dist <= 0.015 :
            if data_node_v3[j]["intersection"] == "true" :
                a.append(j)
                print("append")
            else :
                b.append(j)
                if dist < min :
                    min = dist
                    minIndex = len(b)-1
                
    for index in a :
        for k in range(len(data_way)):
            # add first traffic signal tag in "way" database
            for kk in range(len(data_node_v3[index]["tag"])) :
                if data_node_v3[index]["tag"][kk]["way"] == data_way[k]["id"] :
                    #check if this way's device has been added
                    num = 1
                    while True :
                        if "Device"+str(num) not in data_way[k].keys() :
                            data_way[k]["Device"+str(num)] = {}
                            data_way[k]["Device"+str(num)]["id"] = i[0]
                            data_way[k]["Device"+str(num)]["ICName"] = i[1]["ICName"]
                            data_way[k]["Device"+str(num)]["closestNodeID"] = data_node_v3[index]["id"]
                            print("add device", num)
                            break
                        else :
                            if data_way[k]["Device"+str(num)]["id"] == i[0] :
                                    print("same!")
                                    break
                        num = num+1
    # not a intersection, but has a device
    if len(a) == 0 and len(b) != 0 :
        index = b[minIndex]
        if len(b) != 1:
            print("not 1")
        data_node_v3[b[minIndex]]["intersection"] = "true"
        for k in range(len(data_way)):
            # add first traffic signal tag in "way" database
            for kk in range(len(data_node_v3[index]["tag"])) :
                if data_node_v3[index]["tag"][kk]["way"] == data_way[k]["id"] :
                    #check if this way's device has been added
                    num = 1
                    while True :
                        if "Device"+str(num) not in data_way[k].keys() :
                            data_way[k]["Device"+str(num)] = {}
                            data_way[k]["Device"+str(num)]["id"] = i[0]
                            data_way[k]["Device"+str(num)]["ICName"] = i[1]["ICName"]
                            data_way[k]["Device"+str(num)]["closestNodeID"] = data_node_v3[index]["id"]
                            print("add device", num)
                            break
                        else :
                            if data_way[k]["Device"+str(num)]["id"] == i[0] :
                                    print("same!")
                                    break
                        num = num+1


# file in
f = open("result_way_traffic_signal_v2.json","w+",encoding="utf-8")
f.write(json.dumps(data_way, ensure_ascii=False, indent=1)) 
f.close()

f = open("result_named_node_v3.json","w+",encoding="utf-8")
f.write(json.dumps(data_node_v3, ensure_ascii=False, indent=1)) 
f.close()






