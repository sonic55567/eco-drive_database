import json
from jmespath import search

data = open("node_v8.json","rb").read()
data_node = json.loads(data)

data = open("node_index.json","rb").read()
data_index = json.loads(data)

data = open("converted.json","rb").read()
data_traffic = json.loads(data)

count = 0
# change Phase's value from list to integer
for i in data_index :
    if "Phase" in data_node[str(i)].keys() :
        for j in data_node[str(i)]["Phase"].keys() :
            data_node[str(i)]["Phase"][str(j)] = 1





f = open("node_v9.json","w+",encoding="utf-8")
f.write(json.dumps(data_node, ensure_ascii=False, indent=1)) 
f.close()


