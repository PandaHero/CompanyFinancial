import csv
import os
import urllib.request
from urllib.parse import urlencode

baseUrl = "http://api.map.baidu.com/panorama/v2?"

ak = "WzNUBwihEnT3EDExNsUENY8SGm5ryH45"
file_path = r"C:\Users\chen\Desktop\新建文件夹"


def get_url(location):
    for pitch in range(0, 120, 30):
        for heading in range(0, 360, 30):
            params = {"ak": ak,
                      "width": "512", "height": "256", "location": location, "fovy": "30",
                      "heading": heading, "pitch": pitch}
            url = baseUrl + urlencode(params)
            yield url


def read_from_csv():
    with open(r"C:\Users\chen\Desktop\新建 Microsoft Excel 工作表.csv", "r+") as file:
        reader = csv.reader(file)
        for row in reader:
            yield str(row[0]) + "," + str(row[-1])


def main():
    dir_num = 1
    for location in read_from_csv():
        imag_num = 1
        for url in get_url(location):
            # 拼接图片名（包含路径）
            filename = '{}{}{}{}'.format(file_path, os.sep, dir_num, str(imag_num) + ".png")
            # 下载图片，并保存到文件夹中
            urllib.request.urlretrieve(url, filename=filename)
            print("第" + str(imag_num * dir_num) + "图片写入成功")
            imag_num += 1
        dir_num += 1


if __name__ == '__main__':
    main()