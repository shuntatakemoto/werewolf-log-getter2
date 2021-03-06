import re
import json

for i in range(1, 31):
    log_data = {}
    message_data = []
    str = ""
    with open("log/log-{}.txt".format(i)) as f:
        for s in f:
            str += s
    str = str.replace(':null', ':"null"')
    eliminated_str = "公開されていない村です"
    pat = "var message = (\[[^\]]+\])"
    pat2 = re.compile(pat, re.MULTILINE)
    ret = pat2.search(str)
    is_eliminated = str.find(eliminated_str)
    white_win = "人狼が全滅しました!【村人チーム】の勝利です!"
    black_win = "人狼が村人の数より多くなりました!【人狼チーム】の勝利です!"
    winner = ""

    if ret:
        str2 = ret.group(1)
        b = eval(str2)
        n = len(b)
        for j in range(n):
            message_data.append([j, b[j]["from_user"], "->", b[j]
                                 ["to_user"], b[j]["job"], b[j]["message"]])
            if b[j]["message"] == white_win:
                winner = "村人"
            elif b[j]["message"] == black_win:
                winner = "人狼"

    log_data["log_id"] = i
    log_data["winner"] = winner
    log_data["message"] = message_data

    if is_eliminated == -1 and len(str) >= 15000 and winner != "":
        with open("json/log-{}.json".format(i), "w") as f:
            log_json = json.dump(log_data, f, indent=4, ensure_ascii=False)
