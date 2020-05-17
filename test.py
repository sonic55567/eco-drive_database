import json
from jmespath import search

data = open("node_v4.json","rb").read()
data_node = json.loads(data)

data = open("node_index.json","rb").read()
data_index = json.loads(data)

print(len(data_node))
print(len(data_index))

i=0
while i<len(data_index) :
    if len(data_node[str(data_index[i])]["Road"]) == 0 :
        del data_node[str(data_index[i])]
        del data_index[i]
    else :
        i=i+1

print(len(data_node))
print(len(data_index))

#######################################################

for i in data_index :
    if data_node[str(i)]["intersection"] == True :
        del data_node[str(i)]["NextIC"]
        if "Phase" in data_node[str(i)].keys() :
            del data_node[str(i)]["Phase"]


#con = "[?type2 == 'asd']"

#res = search(con, data_json)
#res["type"] = "asd"

f = open("node_v6.json","w+",encoding="utf-8")
f.write(json.dumps(data_node, ensure_ascii=False, indent=1)) 
f.close()

f = open("node_index_v2.json","w+",encoding="utf-8")
f.write(json.dumps(data_index, ensure_ascii=False, indent=1)) 
f.close()


