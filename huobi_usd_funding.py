import requests
import time

aver = 0
kind = 0
total_sum = 0
times = 0

get_contract_info_url = "https://api.hbdm.com/swap-api/v1/swap_contract_info"
res = requests.get(get_contract_info_url)
contract_info = res.json()["data"]

pairs = {}
url = "https://api.hbdm.com/swap-api/v1/swap_historical_funding_rate"
for item in contract_info:
    times = 0
    sum = 0
    kind = kind + 1
    surl = url + "?contract_code=" + item["contract_code"] + "&page_size=50"
    res = requests.get(surl)
    for i in res.json()["data"]["data"]:
        times = times + 1
        sum += float(i["realized_rate"])
    print(item["contract_code"], ":", round(sum, 3), int(times/3), "day", "AverageProfit:", round(sum/(times/3), 5))
    pairs[item["contract_code"]] = round(sum/(times/3), 5)
    total_sum = total_sum + sum/(times/3)
    
aver = total_sum/kind
print("Total kind:", kind, "Average profit:", round(aver, 5))
pairs = sorted(pairs.items(), key=lambda item:item[1])
        
for i in pairs:
    print(i)




