import json
from jmespath import search

data = open("result_way_traffic_signal_v2.json","rb").read()
data_trafficSignal = json.loads(data)
print(len(data_trafficSignal))

for i in range(len(data_trafficSignal)) :
    data_trafficSignal[i]["Device"] = []
    for j in range(len(data_trafficSignal[i]["nodes"])) :
        for k in range(1, 50):
            if "Device"+str(k) in data_trafficSignal[i].keys() :
                if data_trafficSignal[i]["nodes"][j] == data_trafficSignal[i]["Device"+str(k)]["closestNodeID"] :
                    data_trafficSignal[i]["Device"].append(data_trafficSignal[i]["Device"+str(k)])
            else :
                break

# delete Device+str keys
for i in range(len(data_trafficSignal)) :
    for k in range(1, 50) :
        if "Device"+str(k) in data_trafficSignal[i].keys() :
            del data_trafficSignal[i]["Device"+str(k)]

# file in
f = open("way_traffic_signal_sorted.json","w+",encoding="utf-8")
f.write(json.dumps(data_trafficSignal, ensure_ascii=False, indent=1)) 
f.close()