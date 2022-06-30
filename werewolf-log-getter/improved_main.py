import re
import json

eliminated_str = "公開されていない村です"
white_win = "人狼が全滅しました!【村人チーム】の勝利です!"
black_win = "人狼が村人の数より多くなりました!【人狼チーム】の勝利です!"

# for i in range(30, 31):
for i in range(121, 122):
    log_data = {}
    message_data = []
    str = ""
    with open("log/log-{}.txt".format(i)) as f:
        for s in f:
            str += s
            if re.search('var message = ', s):
                str_array=s

    str = str.replace(':null', ':"null"')
    str_array = str_array.replace(':null', ':"null"')
    is_eliminated = str.find(eliminated_str)
    winner = ""
    
    srt_array_deleted_forward=str_array[18:]
    str_array_deleted_back=srt_array_deleted_forward[:-2]
    b=eval(str_array_deleted_back)

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
