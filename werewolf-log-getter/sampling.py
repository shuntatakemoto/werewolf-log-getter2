# /jsonから人狼知能レギュレーションに沿った5あるいは15人のゲームを抽出する

import re
import json

for i in range(1, 4):
    log_data = {}
    file_number_five = 0
    file_number_fifteen = 0
    fp = None
    try:
        fp = open("json/log-{}.json".format(i))

    except FileNotFoundError:
        pass
    if fp:
        jsn = json.load(fp)
        log_data["jobs"] = jsn["jobs"]
        log_data["log_id"] = jsn["log_id"]
        log_data["winner"] = jsn["winner"]
        log_data["message"] = jsn["message"]

        if jsn["jobs"] == "役職設定【人狼-1,占い師-1,狂人-1,村人-2,役欠け:なし】":
            file_number_five += 1
            with open("json_five/log-{}.json".format(file_number_five), "w") as f:
                log_json = json.dump(
                    log_data, f, indent=4, ensure_ascii=False)

        elif jsn["jobs"] == "役職設定【人狼-3,占い師-1,狩人-1,霊能者-1,狂人-1,村人-8,役欠け:なし】":
            file_number_fifteen += 1
            with open("json_fifteen/log-{}.json".format(file_number_fifteen), "w") as f:
                log_json = json.dump(
                    log_data, f, indent=4, ensure_ascii=False)
