import math
import json
from jmespath import search

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
    for j in range(len(data_node_v3)) :
        a = math.sqrt(pow(data_node_v3[j]["lat"]-x, 2) + pow(data_node_v3[j]["lon"]-y, 2))
        if a <= min:
            min = a
            index = j   # the closest node index
    min = 10000
    
    #if data_node_v3[index]["intersection"] == True :
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
    '''
    else :
        # the traffic signal which not at the head or tail
        for k in range(len(data_way)):
            # add first traffic signal tag in "way" database
            if data_node_v3[index]["tag"][0]["way"] == data_way[k]["id"] :
                num = 1
                while True :
                    if "Device"+str(num) not in data_way[k].keys() :
                        data_way[k]["Device"+str(num)] = {}
                        data_way[k]["Device"+str(num)]["id"] = i[0]
                        data_way[k]["Device"+str(num)]["ICName"] = i[1]["ICName"]
                        data_way[k]["Device"+str(num)]["closestNodeID"] = data_node_v3[index]["id"]
                        data_way[k]["Device"+str(num)]["middle"] = True
                        print("add device", num)
                        break
                    else :
                        if data_way[k]["Device"+str(num)]["id"] == i[0] :
                            print("same!")
                            break
                    num = num+1
                break
        print("device map in middle!")
        notMap = notMap+1
print("there are ", notMap, "devices cannot map to data.")
    '''

# file in
f = open("result_way_traffic_signal_v2.json","w+",encoding="utf-8")
f.write(json.dumps(data_way, ensure_ascii=False, indent=1)) 
f.close()






