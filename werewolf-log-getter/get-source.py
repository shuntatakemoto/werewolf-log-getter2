import requests
import time

# 取得範囲を設定(x,y=int)
for id in range(x, y):
    url = 'https://zinro.net/m/log.php?id='+str(id)
    filename = 'log/log-'+str(id)+".txt"

    urlData = requests.get(url).content

    with open(filename, mode='wb') as f:  # wb でバイト型を書き込める
        # 負荷対策(t=int)
        time.sleep(t)
        f.write(urlData)
