import json
from jmespath import search

data = open("result_named_node_v3.json","rb").read()
data_node = json.loads(data)
convert = dict()


for i in range(len(data_node)) :
    convert[data_node[i]["id"]] = {}
    convert[data_node[i]["id"]]["lat"] = data_node[i]["lat"]
    convert[data_node[i]["id"]]["lon"] = data_node[i]["lon"]
    convert[data_node[i]["id"]]["intersection"] = data_node[i]["intersection"]
    convert[data_node[i]["id"]]["way"] = []
    for j in range(len(data_node[i]["tag"])) :
        convert[data_node[i]["id"]]["way"].append(data_node[i]["tag"][j]["way"])
    


f = open("node_v1.json","w+",encoding="utf-8")
#print(res)
f.write(json.dumps(convert, ensure_ascii=False, indent=1)) 
f.close()

