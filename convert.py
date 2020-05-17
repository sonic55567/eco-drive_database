import json
from jmespath import search


data = open("result.json","rb").read()
data_way = json.loads(data)
data = open("result_node.json","rb").read()
data_node = json.loads(data)

print(len(data_node))
print(len(data_way))
nodeCount = len(data_node)
wayCount = len(data_way)

print(data_node[62445]["id"])


"""
# delete the useless nodes
i = 0
while i<count :
    if len(data_node_name[i]["tags"]) == 1:
        del data_node_name[i]
        i = i-1
        count = count-1
    i = i+1
"""
# add new key in node
for i in range(nodeCount) :
    data_node[i]["intersection"] = "false"

print("add intersection completed")

# add tag list
for i in range(len(data_node)) :
    data_node[i]["tag"] = []

# convert road tags to node
for i in range(wayCount) :
    for j in range(len(data_way[i]["nodes"])) :
        for k in range(nodeCount) :
            if data_way[i]["nodes"][j] == data_node[k]["id"] :
                data_node[k]["tag"].append(data_way[i]["tags"])
                data_node[k]["tag"][-1]["way"] = data_way[i]["id"]
                break

# tag intersection
for i in range(len(data_node)) :
    if len(data_node[i]["tag"]) > 1 :
        data_node[i]["intersection"] = "true"
"""
# useless
for i in range(len(data_node)) :
    for j in range(len(data_way)) :
        for k in range(len(data_way[j]["nodes"])) :
            if data_node[i]["id"] == data_way[j]["nodes"][k] :
                data_node[i]["tags"] = data_way[j]["tags"]
                break

"""


# file in
f = open("result_named_node_v3.json","w+",encoding="utf-8")
#print(res)
f.write(json.dumps(data_node, ensure_ascii=False, indent=1)) 
f.close()
