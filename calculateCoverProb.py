import json
from jmespath import search

data = open("converted.json","rb").read()
data_traffic = json.loads(data)

count = 0
cover = 0
for i in data_traffic["Traffic"].keys():
    for j in data_traffic["Traffic"][str(i)].keys():
        for k in data_traffic["Traffic"][str(i)][str(j)].keys() :
            order = data_traffic["Traffic"][str(i)][str(j)][str(k)]["PhaseOrder"]
            count = count+1
            if (order == "B0") or (order == "00") or (order == "40") or (order == "60") or (order == "A0") or (order == "E2") or (order == "52") or (order == "A2") :
                cover = cover+1

print("Cover rate:", cover*100/count, "%")
            