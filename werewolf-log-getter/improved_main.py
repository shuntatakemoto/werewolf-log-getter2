import re
for i in range(30, 31):
# for i in range(121, 122):
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
    
    str_array_1=str_array.rstrip(";")
    srt_array_deleted=str_array_1[18:]
    str_array_deleted2=srt_array_deleted[:-2]
    b=eval(str_array_deleted2)

    n = len(b)
    for j in range(n):
        message_data.append([j, b[j]["from_user"], "->", b[j]
                                ["to_user"], b[j]["job"], b[j]["message"]])

    log_data["log_id"] = i
    log_data["message"] = message_data
    print("log_data",log_data)
