import json
from jmespath import search

data = open("nodeTest_v4.json","rb").read()
data_node = json.loads(data)

data = open("way_traffic_signal_sorted.json","rb").read()
data_way = json.loads(data)

data = open("node_index.json","rb").read()
data_index = json.loads(data)
convert = dict()
index = list()
phaseMap = dict()
aa = 0
"""
##
for i in range(len(data_index)) :
    for j in range(len(data_node[str(data_index[i])]["way"])) :
        for k in range(len(data_way)) :
            if data_node[str(data_index[i])]["way"][j] == data_way[k]["id"] :
                for l in range(len(data_way[k]["Device"])) :
                    if data_way[k]["Device"][l]["closestNodeID"] == data_index[i] :
                        data_node[str(data_index[i])]["intersection"] = True
                        data_node[str(data_index[i])]["DeviceID"] = data_way[k]["Device"][l]["id"]
                        print(aa)
                        aa = aa+1
                break
# 增加NextIC等欄位


"""
##
# fix intersection key(string to boolean)
for i in data_index :
    if data_node[str(i)]["intersection"] == "true":
        data_node[str(i)]["intersection"] = True
    if data_node[str(i)]["intersection"] == "false":
        data_node[str(i)]["intersection"] = False

deviceID = ""
nodeID = ""

for i in range(len(data_way)) :
    deviceID = ""
    nodeID = ""
    for j in range(len(data_way[i]["nodes"])) :
        if data_node[str(data_way[i]["nodes"][j])]["intersection"] == True :
            if "DeviceID" in  data_node[str(data_way[i]["nodes"][j])].keys() :
                deviceID = data_node[str(data_way[i]["nodes"][j])]["DeviceID"]
                nodeID = str(data_way[i]["nodes"][j])
        else :
            data_node[str(data_way[i]["nodes"][j])]["NextIC"].append(deviceID)
            data_node[str(data_way[i]["nodes"][j])]["NextICCC"].append(nodeID)
            #print(deviceID)
    deviceID = ""
    nodeID = ""
    for j in reversed(range(len(data_way[i]["nodes"]))) :
        if data_node[str(data_way[i]["nodes"][j])]["intersection"] == True :
            if "DeviceID" in  data_node[str(data_way[i]["nodes"][j])].keys() :
                deviceID = data_node[str(data_way[i]["nodes"][j])]["DeviceID"]
                nodeID = str(data_way[i]["nodes"][j])
        else :
            data_node[str(data_way[i]["nodes"][j])]["NextIC"].append(deviceID)
            data_node[str(data_way[i]["nodes"][j])]["NextICCC"].append(nodeID)
# 抓出nextIC


for i in data_index :
    if (data_node[str(i)]["intersection"] == True) and ("DeviceID" in  data_node[str(i)].keys()) :
        data_node[str(i)]["Phase"] = {}
        phaseMap[str(i)] = {}
        for j in range(len(data_node[str(i)]["ConnectedNodes"])) :
            if data_node[str(data_node[str(i)]["ConnectedNodes"][j])]["intersection"] == False :
                for k in range(len(data_node[str(data_node[str(i)]["ConnectedNodes"][j])]["NextIC"])) :
                    
                    if data_node[str(data_node[str(i)]["ConnectedNodes"][j])]["NextIC"][k] != data_node[str(i)]["DeviceID"] :
                        data_node[str(i)]["Phase"][data_node[str(data_node[str(i)]["ConnectedNodes"][j])]["NextIC"][k]] = []
                        data_node[str(i)]["Phase"][data_node[str(data_node[str(i)]["ConnectedNodes"][j])]["NextIC"][k]].append(1)
                        phaseMap[str(i)][data_node[str(data_node[str(i)]["ConnectedNodes"][j])]["NextIC"][k]] = data_node[str(data_node[str(i)]["ConnectedNodes"][j])]["NextICCC"][k]
                        #print("here")
            elif "DeviceID" in data_node[str(data_node[str(i)]["ConnectedNodes"][j])].keys() :
                data_node[str(i)]["Phase"][data_node[str(data_node[str(i)]["ConnectedNodes"][j])]["DeviceID"]] = []
                data_node[str(i)]["Phase"][data_node[str(data_node[str(i)]["ConnectedNodes"][j])]["DeviceID"]].append(1)
                phaseMap[str(i)][data_node[str(data_node[str(i)]["ConnectedNodes"][j])]["DeviceID"]] = str(data_node[str(i)]["ConnectedNodes"][j])


# delete useless key in intersection nodes (NextIC...)
count = 0
for i in data_index :
    if data_node[str(i)]["intersection"] == True :
        del data_node[str(i)]["NextIC"]
        if "DeviceID" in  data_node[str(i)].keys() :
            if "" in data_node[str(i)]["Phase"].keys() :
                count = count+1
                #print("delete the empty device id successfully ", count)
                del data_node[str(i)]["Phase"][""]



f = open("nodeTest_v5.json","w+",encoding="utf-8")
#print(res)
f.write(json.dumps(data_node, ensure_ascii=False, indent=1)) 
f.close()

f = open("phaseMapping.json","w+",encoding="utf-8")
#print(res)
f.write(json.dumps(phaseMap, ensure_ascii=False, indent=1)) 
f.close()
