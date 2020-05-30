import json
from jmespath import search

data = open("node_v5.json","rb").read()
data_node = json.loads(data)

data = open("node_index.json","rb").read()
data_index = json.loads(data)

count = 0

for i in data_index :
    # delete "way" key
    if "way" in data_node[str(i)].keys() :
        del data_node[str(i)]["way"]
    # change key value
    data_node[str(i)]["lat"] = data_node[str(i)].pop("lat")
    data_node[str(i)]["lng"] = data_node[str(i)].pop("lon")
    data_node[str(i)]["Intersection"] = data_node[str(i)].pop("intersection")
    if "NextIC" in data_node[str(i)].keys() :
        data_node[str(i)]["NextIC"] = data_node[str(i)].pop("NextIC")
    if "NextICCC" in data_node[str(i)].keys() :
        data_node[str(i)]["NextICCC"] = data_node[str(i)].pop("NextICCC")
    if "CheckEast" in data_node[str(i)].keys() :
        data_node[str(i)]["CheckEast"] = data_node[str(i)].pop("CheckEast")
    data_node[str(i)]["ConnectedNodes"] = data_node[str(i)].pop("ConnectedNodes")
    data_node[str(i)]["Roads"] = data_node[str(i)].pop("Road")
    if "DeviceID" in data_node[str(i)].keys() :
        data_node[str(i)]["DeviceID"] = data_node[str(i)].pop("DeviceID")
    if "Phase" in data_node[str(i)].keys() :
        data_node[str(i)]["Phase"] = data_node[str(i)].pop("Phase")


f = open("node_v8.json","w+",encoding="utf-8")
f.write(json.dumps(data_node, ensure_ascii=False, indent=1)) 
f.close()
