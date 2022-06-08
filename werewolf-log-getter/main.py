import re
import json

for i in range(16, 17):
    log_data = {}
    message_data = []
    # print("{}番目のゲームの会話".format(i))

    str = ""
    with open("log/log-{}.txt".format(i)) as f:
        for s in f:
            str += s
    str = str.replace(':null', ':"null"')
    pat = "var message = (\[[^\]]+\])"
    pat2 = re.compile(pat, re.MULTILINE)
    ret = pat2.search(str)
    if ret:
        str2 = ret.group(1)
        b = eval(str2)
        n = len(b)
        for j in range(n):
            message_data.append([j, b[j]["from_user"], "->", b[j]
                                 ["to_user"], b[j]["job"], b[j]["message"]])

    log_data["log_id"] = i
    log_data["message"] = message_data
    print(log_data)

    with open("json/log-{}.json".format(i), "w") as f:
        log_json = json.dump(log_data, f, indent=4, ensure_ascii=False)
        print(log_data)
