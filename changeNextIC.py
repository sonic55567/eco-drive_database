import json
from jmespath import search
from math import *

def Distance(lat1,lng1,lat2,lng2):
    radlat1=radians(lat1)  
    radlat2=radians(lat2)  
    a=radlat1-radlat2  
    b=radians(lng1)-radians(lng2)  
    s=2*asin(sqrt(pow(sin(a/2),2)+cos(radlat1)*cos(radlat2)*pow(sin(b/2),2)))  
    earth_radius=6378.137  
    s=s*earth_radius  
    if s<0:  
        return -s  
    else:  
        return s


data = open("node_v9.json","rb").read()
data_node = json.loads(data)

data = open("node_index.json","rb").read()
data_index = json.loads(data)

#change ConnectedNodes type from long to string
for i in data_index :
    for j in range(len(data_node[str(i)]["ConnectedNodes"])) :
        data_node[str(i)]["ConnectedNodes"][j] = str(data_node[str(i)]["ConnectedNodes"][j])

# change NextIC list content (origin : DeviceID, new : NodeID)
for i in data_index :
    if "NextIC" in data_node[str(i)] :
        data_node[str(i)]["NextIC"] = data_node[str(i)]["NextICCC"]
    del data_node[str(i)]["NextICCC"]

                

f = open("node_v10.json","w+",encoding="utf-8")
f.write(json.dumps(data_node, ensure_ascii=False, indent=1)) 
f.close()