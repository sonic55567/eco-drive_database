import json
from jmespath import search

data = open("node_v8.json","rb").read()
data_node = json.loads(data)

data = open("node_index.json","rb").read()
data_index = json.loads(data)

data = open("converted.json","rb").read()
data_traffic = json.loads(data)

count = 0
print("Device :")
for i in data_traffic["Device"]["S059801"].keys() :
    print(i)
print("DeciveWeekday :")
for i in data_traffic["DeviceWeekday"]["S059801"]["1"]["2100"] :
    print(i)
print("Traffic :")
for i in data_traffic["Traffic"]["S059801"].keys() :
    print(i)

"""
f = open("node_v9.json","w+",encoding="utf-8")
f.write(json.dumps(data_node, ensure_ascii=False, indent=1)) 
f.close()
"""

