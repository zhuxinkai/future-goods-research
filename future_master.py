import requests
from make_kline import make_kline
import csv




url = 'http://hq.sinajs.cn/list=M0'

req = requests.get(url)
print(req.text)




url_caipo = 'http://hq.sinajs.cn/list=RM0'
req_caipo = requests.get(url_caipo)
print(req_caipo.text)

url_caipo_date = 'http://hq.sinajs.cn/list=RM2009'
req_caipo_date = requests.get(url_caipo_date)
print(req_caipo_date.text)


# 开始创建csv 表格
# newline='' 解决写入"Date" 行的前后空白行问题。

f = open('data.csv','w',encoding='utf-8',newline='')
csv_writer = csv.writer(f)
csv_writer.writerow([" ","Open","High","Low","Close","Volume"])
#csv_writer.writerow(["Date"])





quotes = []

url_caipo_kline = 'http://stock2.finance.sina.com.cn/futures/api/json.php/IndexService.getInnerFuturesDailyKLine?symbol=RM2009'
req_caipo_kline = requests.get(url_caipo_kline)
print(req_caipo_kline.text)
caipo_kline_datalist = (req_caipo_kline.text[1:-1]).split("],")
print(caipo_kline_datalist)





for i in caipo_kline_datalist:
    print(i)
    #关于索引的位置，求最后一个" 的索引，可以指定返回的索引段，而且最后一个索引可以超出当前字符串的索引长度而不报错。
    lastindex = (i.index("\"",59,67))
    sdate_plt = i[2:12]

    sopen = i[15:23]
    shigh = i[26:34]
    slow = i[37:45]
    sclose = i[48:56]
    mountdaily = i[59:lastindex]

    csv_writer.writerow([sdate_plt, sopen, shigh, slow, sclose,mountdaily])


f.close()


make_kline('data.csv')