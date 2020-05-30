import json
from jmespath import search

data = open("result.json","rb").read()
data_road = json.loads(data)

output = dict()

for i in data_road :
    if "name" in i["tags"].keys() :
        output[i["tags"]["name"]] = i["tags"]["highway"]

f = open("RoadHierarchy.json","w+",encoding="utf-8")
f.write(json.dumps(output, ensure_ascii=False, indent=1)) 
f.close()
