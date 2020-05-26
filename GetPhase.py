import json
from jmespath import search

data = open("node_v5.json","rb").read()
data_node = json.loads(data)

data = open("node_index.json","rb").read()
data_index = json.loads(data)

count = 0
# delete useless key in intersection nodes (NextIC...)
for i in data_index :
    if data_node[str(i)]["intersection"] == True :
        del data_node[str(i)]["NextIC"]
        if "DeviceID" in  data_node[str(i)].keys() :
            if "" in data_node[str(i)]["Phase"].keys() :
                count = count+1
                print("delete the empty device id successfully ", count)
                del data_node[str(i)]["Phase"][""]
            for j in  data_node[str(i)]["Phase"] :
                data_node[str(i)]["Phase"][str(j)].append(1)




f = open("node_v6.json","w+",encoding="utf-8")
f.write(json.dumps(data_node, ensure_ascii=False, indent=1)) 
f.close()
