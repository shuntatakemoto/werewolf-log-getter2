import json
import pandas as pd

table = []
for i in range(1, 850000):
    log = []
    fp = None
    try:
        fp = open("json/log-{}.json".format(i))

    except FileNotFoundError:
        pass
    if fp:
        jsn = json.load(fp)
        log.append(jsn["log_id"])
        log.append(len(jsn["message"]))
        table.append(log)

print(table)

# tableを表に変換する
df = pd.DataFrame(table)
df.columns = ['log_id', 'total_message']
print(df)
