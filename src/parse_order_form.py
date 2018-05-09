import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from bs4 import BeautifulSoup
import pymongo

# 连接pymongo
client = pymongo.MongoClient(host="localhost", port=27017)
# 指定数据库名称
db = client.test
# 指定数据库中的集合
orderForm = db.OrderDetail
receiveForm = db.ReceiveDetail
pageForm = db.PageNum
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


def get_form_info(pageNum):
    url = "https://auchan.chinab2bi.com/auchan/buyGrnQry/detail.hlt?grnid=" + str(pageNum)
    # 解决sslerror
    try:
        req = requests.get(url, headers=headers)
    except requests.exceptions.SSLError as err:
        req = requests.get(url, headers=headers, verify=False)
    soup = BeautifulSoup(req.text, "lxml")
    # 解析收货单
    panelBody = soup.find_all("td", {"class": "panel-body"})
    # 收货单的标签和特征值
    receiveFormLabel = [label.get_text() for label in panelBody[0].find_all("td", {"class": "form_label"})]
    receiveFormValue = [value.get_text() for value in panelBody[0].find_all("td", {"width": "30%"})]
    receiveFormValue.insert(5, panelBody[0].find("td", {"colspan": "3"}).get_text())
    # 解析订货单
    panelOdd = panelBody[-1].find_all("tr", {"class": "odd"})
    panelEven = panelBody[-1].find_all("tr", {"class": "even"})
    # 订货单明细标签
    # orderDetailLabel = ["序号", "商品号", "商品名称", "税率", "单价", "订单数量", "收货数量", "金额"]
    # 订货单明细特征值
    orderDetailValue = []
    for item in panelOdd:
        tdItems = item.find_all("td")
        value = []
        for tdItem in tdItems:
            value.append(tdItem.get_text().replace("\r\n", "").replace("\t", ""))
        orderDetailValue.append(value)
    for item in panelEven:
        tdItems = item.find_all("td")
        value = []
        for tdItem in tdItems:
            value.append(tdItem.get_text().replace("\r\n", "").replace("\t", ""))
        orderDetailValue.append(value)
    return receiveFormLabel, receiveFormValue, orderDetailValue


if __name__ == '__main__':
    page_num = pageForm.find({'pagenum': {'$gt': 102328065}})
    for num in page_num:
        print(get_form_info(num["pagenum"]))
