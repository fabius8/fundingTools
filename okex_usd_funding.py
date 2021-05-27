import requests
import time

url = "https://okex.com/api/swap/v3/instruments"
res = requests.get(url)

aver = 0
kind = 0
total_sum = 0

pairs = {}

for simbol in res.json():
    if "USDT-SWAP" in simbol["instrument_id"]:
        continue
    kind = kind + 1
    url = "https://okex.com/api/swap/v3/instruments/" + simbol["instrument_id"] + "/historical_funding_rate"
    #print(url)
    res = requests.get(url)
    sum = 0
    times = 0
    for i in res.json():
        times = times + 1
        sum += float(i["funding_rate"])
    print(simbol["instrument_id"], ":", round(sum, 3), int(times/3), "day", "AverageProfit:", round(sum/(times/3), 5))
    pairs[simbol["instrument_id"]] = round(sum/(times/3), 5)
    total_sum = total_sum + sum/(times/3)
    #time.sleep(1)

aver = total_sum/kind
print("Total kind:", kind, "Average profit:", round(aver, 5))
pairs = sorted(pairs.items(), key=lambda item:item[1])
for i in pairs:
    print(i)

