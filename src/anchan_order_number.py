import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import time
import pymongo

# 连接pymongo
client = pymongo.MongoClient(host="localhost", port=27017)
# 指定数据库名称
db = client.test
# 指定数据库中的集合名称
pageNumSet = db.PageNum
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
           "Accept-Encoding": "gzip, deflate,br",
           "Accept-Language": "zh-CN,zh;q=0.9",
           "Cache-Control": "max-age=0",
           "Connection": "keep-alive",
           "Cookie": "BIGipServerpool_auchan_7101=708184586.48411.0000; JSESSIONID=PC4hhyrZK0BnFTJv3g7prhKpLdyBwDVy0hcy2xF2zmN1Tnf67hVJ!-1997790883",
           "Host": "auchan.chinab2bi.com",
           "Referer": "https://auchan.chinab2bi.com/common/index.jsp",
           "Upgrade-Insecure-Requests": "1",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36"}

startTime = time.time()
count = 0
for i in range(104829280, 999999999, 1):
    numPage = i + count
    url = "https://auchan.chinab2bi.com/auchan/buyGrnQry/detail.hlt?grnid=" + str(numPage)
    # 解决sslerror
    try:
        req = requests.get(url, headers=headers)
    except requests.exceptions.SSLError as err:
        # print(err)
        req = requests.get(url, headers=headers, verify=False)

    if "退货单明细列表" in req.text:
        # print(req.text)
        data = {"pagenum": numPage}
        pageNumSet.insert_one(data)
        print(numPage)
        startTime = time.time()

    else:
        endTime = time.time()
        print(endTime - startTime)
        print(numPage)
        if endTime - startTime > 10:
            count += 60
            startTime = endTime
