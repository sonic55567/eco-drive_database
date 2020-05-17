import json
from jmespath import search



data = open("result_named_node_v3.json","rb").read()
data_node_v3 = json.loads(data)

data = open("converted.json","rb").read()
data_signal = json.loads(data)

count = len(data_node_v3)
CC = 0
for i in range(count) :
    if len(data_node_v3[i]["tag"]) == 0:
        print(i)
#print(len(data_node_v3[0]["tag"]))


for i in data_signal["Device"].items():
    print(i[0],"\n")
    CC = CC+1

print(CC)


"""
for i in range(count):
    if data_node[i]["intersection"] == "true":
        data_node[i]["intersection"] = True
    else:
        data_node[i]["intersection"] = False

"""
"""
# delete the useless nodes
i = 0
while i<count :
    if len(data_node[i]["tags"]) == 1:
        del data_node[i]
        i = i-1
        count = count-1
    i = i+1
"""
"""
# file in
f = open("result_named_node_v2.json","w+",encoding="utf-8")
#print(res)
f.write(json.dumps(data_node, ensure_ascii=False, indent=1)) 
f.close()
"""

