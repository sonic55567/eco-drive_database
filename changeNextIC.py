import json
from jmespath import search

data = open("node_v9.json","rb").read()
data_node = json.loads(data)

data = open("node_index.json","rb").read()
data_index = json.loads(data)

#change ConnectedNodes type from long to string
for i in data_index :
    for j in range(len(data_node[str(i)]["ConnectedNodes"])) :
        data_node[str(i)]["ConnectedNodes"][j] = str(data_node[str(i)]["ConnectedNodes"][j])


f = open("node_v10.json","w+",encoding="utf-8")
f.write(json.dumps(data_node, ensure_ascii=False, indent=1)) 
f.close()