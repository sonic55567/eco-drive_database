import json
from jmespath import search

data = open("converted.json","rb").read()
data_traffic = json.loads(data)

# afternoon
count = 0
cover = 0
for i in data_traffic["DeviceWeekday"].keys():                          # deviceID
    for j in data_traffic["DeviceWeekday"][str(i)].keys():              # 
        index = 0
        planID = ""
        for k in data_traffic["DeviceWeekday"][str(i)][str(j)].keys():  # time
            time = data_traffic["DeviceWeekday"][str(i)][str(j)][str(k)]["Time"]
            if time<=1230:
                if index < time :
                    index = time
                    planID = data_traffic["DeviceWeekday"][str(i)][str(j)][str(k)]["PlanID"]
        # time
        if i in data_traffic["Traffic"].keys():
            if (len(planID)==1) and (planID not in data_traffic["Traffic"][str(i)].keys()):
                planID = "0"+planID
            if planID in data_traffic["Traffic"][str(i)].keys():
                for k in data_traffic["Traffic"][str(i)][planID].keys():
                    order = data_traffic["Traffic"][str(i)][planID][str(k)]["PhaseOrder"]
                    count = count+1
                    if (order == "B0") or (order == "00") or (order == "40") or (order == "60") or (order == "52") or (order == "A0") or (order == "E2") or (order == "52") or (order == "A2") :
                        cover = cover+1
        break
print("Cover rate in the afternoon:", cover*100/count, "%")

# evening
count = 0
cover = 0
for i in data_traffic["DeviceWeekday"].keys():                          # deviceID
    for j in data_traffic["DeviceWeekday"][str(i)].keys():              # 
        index = 0
        planID = ""
        for k in data_traffic["DeviceWeekday"][str(i)][str(j)].keys():  # time
            time = data_traffic["DeviceWeekday"][str(i)][str(j)][str(k)]["Time"]
            if time<=1730:
                if index < time :
                    index = time
                    planID = data_traffic["DeviceWeekday"][str(i)][str(j)][str(k)]["PlanID"]
        # time
        if i in data_traffic["Traffic"].keys():
            if (len(planID)==1) and (planID not in data_traffic["Traffic"][str(i)].keys()):
                planID = "0"+planID
            if planID in data_traffic["Traffic"][str(i)].keys():
                for k in data_traffic["Traffic"][str(i)][planID].keys():
                    order = data_traffic["Traffic"][str(i)][planID][str(k)]["PhaseOrder"]
                    count = count+1
                    if (order == "B0") or (order == "00") or (order == "40") or (order == "60") or (order == "52") or (order == "A0") or (order == "E2") or (order == "52") or (order == "A2") :
                        cover = cover+1
        break
print("Cover rate in the evening:", cover*100/count, "%")
            