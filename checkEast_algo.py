import json
from jmespath import search

data = open("nodeTest_v5.json","rb").read()
data_node = json.loads(data)

data = open("node_index.json","rb").read()
data_index = json.loads(data)

for i in data_index :
    if data_node[str(i)]["intersection"] == False :
        if len(data_node[str(i)]["ConnectedNodes"]) == 2 and len(data_node[str(i)]["NextIC"]) == 2 :
            lat = data_node[str(i)]["lat"]
            lon = data_node[str(i)]["lon"]
            lat1 = data_node[str(data_node[str(i)]["ConnectedNodes"][0])]["lat"]
            lon1 = data_node[str(data_node[str(i)]["ConnectedNodes"][0])]["lon"]
            lat2 = data_node[str(data_node[str(i)]["ConnectedNodes"][1])]["lat"]
            lon2 = data_node[str(data_node[str(i)]["ConnectedNodes"][1])]["lon"]
            if (lat1-lat) * (lat2-lat) > 0 :
                data_node[str(i)]["CheckEast"] = True
                print("checkEast is true nowww")
                if lon1-lon < 0 :
                    data_node[str(i)]["ConnectedNodes"][0], data_node[str(i)]["ConnectedNodes"][1] = data_node[str(i)]["ConnectedNodes"][1], data_node[str(i)]["ConnectedNodes"][0]
                    data_node[str(i)]["NextIC"][0], data_node[str(i)]["NextIC"][1] = data_node[str(i)]["NextIC"][1], data_node[str(i)]["NextIC"][0]
                    data_node[str(i)]["NextICCC"][0], data_node[str(i)]["NextICCC"][1] = data_node[str(i)]["NextICCC"][1], data_node[str(i)]["NextICCC"][0]
                    print("eastSwapped!!")
            else :
                # need to swap
                if lat1-lat < 0 :
                    data_node[str(i)]["ConnectedNodes"][0], data_node[str(i)]["ConnectedNodes"][1] = data_node[str(i)]["ConnectedNodes"][1], data_node[str(i)]["ConnectedNodes"][0]
                    data_node[str(i)]["NextIC"][0], data_node[str(i)]["NextIC"][1] = data_node[str(i)]["NextIC"][1], data_node[str(i)]["NextIC"][0]
                    data_node[str(i)]["NextICCC"][0], data_node[str(i)]["NextICCC"][1] = data_node[str(i)]["NextICCC"][1], data_node[str(i)]["NextICCC"][0]
                    print("swapped")

f = open("node_v5.json","w+",encoding="utf-8")
#print(res)
f.write(json.dumps(data_node, ensure_ascii=False, indent=1)) 
f.close()
