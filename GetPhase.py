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

min = 999
for i in data_index :
    if "Phase" in data_node[str(i)].keys() :    # aka intersection == true
        # intersection which has no other roads intersect doesn't need to edit 
        if len(data_node[str(i)]["Roads"]) != 1 :
            # get device name
            deviceName = data_traffic["Device"][data_node[str(i)]["DeviceID"]]["ICName"]
            if deviceName.find("小東路") != -1 :
                print(deviceName)
            # get 
            for j in data_node[str(i)]["Roads"] :
                index = deviceName.find(str(j))
                #print(index)
                if index != -1 :
                    if index < min :
                        min = index
                        target = str(j)
                        print(target)
                if index == 0 :
                    target = str(j)
                    break
            for j in data_node[str(i)]["ConnectedNodes"] :
                if "Phase" in data_node[str(j)].keys() :
                    for k in data_node[str(j)]["Roads"] :
                        if k == target :
                            data_node[str(i)]["Phase"][data_node[str(j)]["DeviceID"]] = 0
                            break

                elif data_node[str(j)]["Intersection"] == False :
                    for k in data_node[str(j)]["Roads"] :
                        if k == target :
                            print("target hit!")
                            print(target)
                            for kk in data_node[str(j)]["NextIC"] :
                                if kk != "" and kk != data_node[str(i)]["DeviceID"] :
                                    data_node[str(i)]["Phase"][str(kk)] = 0
                                    print("change!")
        else :
            for j in data_node[str(i)]["Phase"].keys() :
                data_node[str(i)]["Phase"][str(j)] = 0

                    

                



f = open("node_v9.json","w+",encoding="utf-8")
f.write(json.dumps(data_node, ensure_ascii=False, indent=1)) 
f.close()


