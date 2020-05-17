import math
import time
import json
from jmespath import search

data = open("result_named_node_v2.json","rb").read()
data_node_v2 = json.loads(data)

count = len(data_node_v2)

x = 22.983118
y = 120.237197

print("There is ", count, " nodes")

start = time.time()
min = 10000
index = -1
for i in range(len(data_node_v2)):
    a = math.sqrt(pow(data_node_v2[i]["lat"]-x, 2) + pow(data_node_v2[i]["lon"]-y, 2))
    if a <= min:
        min = a
        index = i

if data_node_v2[index]["intersection"] == True :
    print("asd")


end = time.time()
"""
c = math.sqrt(pow(23.0006269-x, 2) + pow(120.2222247-y, 2))
d = math.sqrt(pow(data_node_v2[0]["lat"]-x, 2) + pow(data_node_v2[0]["lon"]-y, 2))
e = math.sqrt(pow(23.3065449-x, 2) + pow(120.6009167-y, 2))
print(c)
print(d)
print(e<c)
"""

print("use ", (end-start), " sec")

print(min)
print(data_node_v2[index])
