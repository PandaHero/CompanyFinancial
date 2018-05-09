# import csv
# import time
#
# start_time = time.time()
# with open(r"C:\Users\chen\Desktop\100013_2017销售商品清单.csv", "r") as file:
#     # 获取csv读取器
#     csv_reader = csv.DictReader(file)
#     for row in csv_reader:
#         print(row)
# end_time = time.time()
# print(end_time - start_time)
import csv

import xlrd
import os

path = r"C:\Users\chen\Desktop\新建文件夹 (2)"

store_num = {"奥莱店": 19045,  "北海店": 19218, "大望路店": 19078, "东直门店": 19099, "蓝港店": 19095, "三里屯店": 19089,
             "顺义欧陆店": 19094, "通州北苑店": 19079, "万寿路店": 19071, "西单店": 19080, "小黄庄店": 19088, "宣武门店": 19076, "颐堤港店": 19069,
             "育慧里店": 91061, "中粮店": 19040}


# 获取文件夹下所有文件名称
def get_path_file_name(path):
    l = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if os.path.splitext(file)[1] == '.xls':
                l.append(os.path.join(root, file))
    return l


# 读取指定表名称的excel
def read_excel_file(book_name, sheet_name):
    # 获取excel文件中的店名
    store_name = book_name[book_name.find("表") + 2:book_name.find("店") + 1].replace(" ","")
    # print(store_name)
    book = xlrd.open_workbook(book_name)
    # 读取指定文件(表)名称的excel
    sheet = book.sheet_by_name(sheet_name)
    # 行数
    nrows = sheet.nrows
    # 列数
    ncols = sheet.ncols
    # 第0行的值
    colName = sheet.row_values(0)
    # 创建空列表保存数据
    sheet_list = []
    for x in range(1, nrows):
        row = sheet.row_values(x)
        if row:
            dict_1 = {}
            for y in range(0, ncols):
                dict_1[colName[y]] = row[y]
            sheet_list.append(dict_1)
    return store_name, sheet_list


def parse_cgz_sheet(book):
    gw_store_num = []
    # info = {}
    store_name, sheet_list = read_excel_file(book, "采购组汇总")
    for item in sheet_list:
        # info["店名"] = store_name
        # info["业种代码"] = item["业种代码"]
        # info["业种"] = item["业种"]
        # info["柜位面积"] = item["柜位面积"]
        gw_store_num.append({"店名": store_name, "业种": "柜位", "业种代码": item["业种代码"], "面积": item["柜位面积"]})

    return gw_store_num


def parse_area_sheet(book):
    store_name, sheet_list = read_excel_file(book, "面积")
    area_store_num = []
    for item in sheet_list:
        if item[''] == "全店建筑面积":
            # print(item)
            # print(store_name)
            area_store_num.append({"店名": store_name, "业种": "建筑", "业种代码": "全店", "面积": item["全店"]})
            area_store_num.append({"店名": store_name, "业种": "建筑", "业种代码": "超市", "面积": item["超市"]})
            area_store_num.append({"店名": store_name, "业种": "建筑", "业种代码": "租赁", "面积": item["租赁"]})
            # print(item["全店"], item["超市"], item["租赁"])
        if item[''] == "经营面积":
            # print(item)
            # print(item["全店"], item["超市"], item["租赁"])
            area_store_num.append({"店名": store_name, "业种": "经营", "业种代码": "全店", "面积": item["全店"]})
            area_store_num.append({"店名": store_name, "业种": "经营", "业种代码": "超市", "面积": item["超市"]})
            area_store_num.append({"店名": store_name, "业种": "经营", "业种代码": "租赁", "面积": item["租赁"]})
        if item[''] == "柜位面积":
            # print(item)
            # print(item["全店"], item["超市"], item["租赁"])
            area_store_num.append({"店名": store_name, "业种": "柜位", "业种代码": "全店", "面积": item["全店"]})
            area_store_num.append({"店名": store_name, "业种": "柜位", "业种代码": "超市", "面积": item["超市"]})
            area_store_num.append({"店名": store_name, "业种": "柜位", "业种代码": "租赁", "面积": item["租赁"]})
    print(area_store_num)
    return area_store_num


def write_to_csv(area_store_num):
    with open(r"C:\Users\chen\Desktop\2018高超门店面积.csv", "a+", newline="", encoding='utf-8') as file:
        tem = 1
        writer = csv.writer(file)
        writer.writerow(["店名", "店号", "业种", "业种代码", "面积"])
        for item in area_store_num:
            num = [item["店名"], store_num[item["店名"]], item["业种"], item["业种代码"], item["面积"]]
            writer.writerow(num)
            print("第" + str(tem) + "次写入成功")
            tem += 1
    print("写入完毕")


if __name__ == '__main__':
    book_list = get_path_file_name(path)
    for book in book_list:
        # print(read_excel_file(book, "面积"))
        cgz_store_num = parse_cgz_sheet(book)
        area_store_num = parse_area_sheet(book)
        area_store_num.extend(cgz_store_num)
        write_to_csv(area_store_num)
