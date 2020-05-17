import json
from jmespath import search

data = open("result_named_node_v3.json","rb").read()
data_node = json.loads(data)

data = open("way_traffic_signal_sorted.json","rb").read()
data_way = json.loads(data)
convert = dict()
index = list()


for i in range(len(data_node)) :
    index.append(data_node[i]["id"])
    convert[data_node[i]["id"]] = {}
    convert[data_node[i]["id"]]["lat"] = data_node[i]["lat"]
    convert[data_node[i]["id"]]["lon"] = data_node[i]["lon"]
    convert[data_node[i]["id"]]["intersection"] = data_node[i]["intersection"]
    convert[data_node[i]["id"]]["way"] = []
    convert[data_node[i]["id"]]["NextIC"] = []
    convert[data_node[i]["id"]]["CheckEast"] = False
    convert[data_node[i]["id"]]["ConnectedNodes"] = []
    convert[data_node[i]["id"]]["Road"] = []
    for j in range(len(data_node[i]["tag"])) :
        convert[data_node[i]["id"]]["way"].append(data_node[i]["tag"][j]["way"])
        if "name" in data_node[i]["tag"][j].keys() :
            convert[data_node[i]["id"]]["Road"].append(data_node[i]["tag"][j]["name"])
    for l in range(len(data_node[i]["tag"])) :
        for j in range(len(data_way)) :
            if data_way[j]["id"] == data_node[i]["tag"][l]["way"] :
                for k in range(len(data_way[j]["nodes"])) :
                    if(data_way[j]["nodes"][k] == data_node[i]["id"]) :
                        if k == 0 :
                            convert[data_node[i]["id"]]["ConnectedNodes"].append(data_way[j]["nodes"][k+1])
                            break
                        elif k == len(data_way[j]["nodes"])-1 :
                            convert[data_node[i]["id"]]["ConnectedNodes"].append(data_way[j]["nodes"][k-1])
                            break
                        else :
                            convert[data_node[i]["id"]]["ConnectedNodes"].append(data_way[j]["nodes"][k-1])
                            convert[data_node[i]["id"]]["ConnectedNodes"].append(data_way[j]["nodes"][k+1])
                            break
                break
    

f = open("node_v2.json","w+",encoding="utf-8")
#print(res)
f.write(json.dumps(convert, ensure_ascii=False, indent=1)) 
f.close()
f = open("node_index.json","w+",encoding="utf-8")
#print(res)
f.write(json.dumps(index, ensure_ascii=False, indent=1)) 
f.close()