import re

message_data = []
for i in range(799930, 799936):
    # game_id = "{}番目のゲームの会話".format(i)
    # message_data.append(game_id)
    print("{}番目のゲームの会話".format(i))
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
        for i in range(n):
            # data = [i, b[i]["from_user"], "->", b[i]
            #         ["to_user"], b[i]["job"], b[i]["message"]]
            # message_data.append(data)
            print(i, b[i]["from_user"], "->", b[i]
                  ["to_user"], b[i]["job"], b[i]["message"])

# print(message_data)
