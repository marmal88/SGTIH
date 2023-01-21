import json
import pandas as pd

with open("data.json") as f:
    data = json.load(f)
    df = pd.json_normalize(data)
    print(df.head())
    # for each in data:
    #     print(each)

# print(json.load("/home/oem/Documents/coding/personal/sgtih/data.json"))
