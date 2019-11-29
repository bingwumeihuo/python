from bs4 import BeautifulSoup
import requests

data = open("F:\code\python\data.txt", 'w+')
url = "https://fangjia.fang.com/pghouse-c0hz/h315-s11-kw%E4%B8%B4%E5%AE%89/"
f = requests.get(url)  # Get该网页从而获取该html内容
soup = BeautifulSoup(f.content, "lxml")  # 用lxml解析器解析该网页的内容, 好像f.text也是返回的html
for k in soup.find_all('span', class_='housetitle'):  # ,找到div并且class为pl2的标签
    a = k.find_all('a')  # 在每个对应div标签下找span标签，会发现，一个a里面有四组span
    # data.write(a[0].string)
# 取第一组的span中的字符串
for c in soup.find_all('p', class_='mt8'):  # ,找到div并且class为pl2的标签
    for d in c.find_all_next('span', class_='pl5'):
        a = (d.get('title'))
        # 将结果写入txt并换行
        s = set(a)
        t = list(s)
        data.write(a + '\n')
        print(t.sort())
