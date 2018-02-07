import csv
import json
# 公司基本信息
import time

import requests

basic_info = ("公司法定中文名称", "公司法定代表人", "公司注册地址", "公司办公地址邮政编码",
              "公司国际互联网网址", "公司董事会秘书姓名", "公司董事会秘书电话", "公司董事会秘书电子信箱",
              "报告期末股东总数", "每10股送红股数", "每10股派息数（含税）", "每10股转增数",
              "本期营业收入(元)", "本期营业利润(元)", "利润总额(元)", "归属于上市公司股东的净利润(元)",
              "归属于上市公司股东的扣除非经常性损益的净利润(元)", "经营活动产生的现金流量净额(元)", "总资产(元)", "所有者权益（或股东权益）(元)",
              "基本每股收益(元/股)", "稀释每股收益(元/股)", "扣除非经常性损益后的基本每股收益(元/股)", "全面摊薄净资产收益率（%）",
              "加权平均净资产收益率（%）", "扣除非经常性损益后全面摊薄净资产收益率（%）", "扣除非经常性损益后的加权平均净资产收益率（%）",
              "每股经营活动产生的现金流量净额(元/股)", "归属于上市公司股东的每股净资产（元/股）")
# 股本结构
stock_structure = ("国家持有的有限售条件流通股份数", "国有法人持有的有限售条件流通股份数", "其他有限售条件的内资流通股份数",
                   "境内法人持有的有限售条件流通股份数", "境内自然人持有的有限售条件流通股份数", "有限售条件的外资流通股份数",
                   "境外法人持有的有限售条件流通股份数", "境外自然人持有的有限售条件流通股份数", "其他有限售股流通股数",
                   "有限售条件流通股数", "无限售条件人民币普通股数", "无限售条件境内上市的外资股数",
                   "无限售条件境外上市的外资股数", "其他无限售条件已上市流通股份数", "无限售条件流通股份合计", "股份总数",
                   "国家持有的有限售条件流通股份占总股本比例(%)", "国有法人持有的有限售条件流通股份占总股本比例(%)",
                   "其他有限售条件的内资流通股份占总股本比例(%)", "境内法人持有的有限售条件流通股份占总股本比例(%)",
                   "境内自然人持有的有限售条件流通股份占总股本比例(%)", "有限售条件的外资流通股份占总股本比例(%)",
                   "境外法人持有的有限售条件流通股份占总股本比例(%)", "境外自然人持有的有限售条件流通股份占总股本比例(%)",
                   "其他有限售股流通股份占总股本比例(%)", "有限售条件流通股占总股本比例(%)", "无限售条件人民币普通股占总股本比例(%)",
                   "无限售条件境内上市的外资股占总股本比例(%)", "无限售条件境外上市的外资股占总股本比例(%)",
                   "其他无限售条件已上市流通股份占总股本比例(%)", "无限售条件流通股占总股本比例(%)", "股份总数占总股本比例(%)")

# 前十大股东
top_ten_shareholder = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")

# 资产负债表
assert_debts = ("货币资金(元)", "结算备付金(元)", "拆出资金(元)", "交易性金融资产(元)", "应收票据(元)", "应收帐款(元)",
                "预付帐款(元)", "应收保费(元)", "应收分保账款(元)", "应收分保合同准备金(元)", "应收利息(元)", "应收股利(元)", "其他应收款(元)",
                "买入返售金融资产(元)", "存货(元)", "一年内到期的非流动资产(元)", "其他流动资产(元)", "流动资产合计(元)", "发放贷款和垫款(元)",
                "可供出售金融资产(元)", "持有至到期投资(元)", "长期应收款(元)", "长期股权投资(元)", "投资性房地产(元)", "固定资产净额(元)",
                "在建工程(元)", "工程物资(元)", "固定资产清理(元)", "生产性生物资产(元)", "油气资产(元)", "无形资产(元)", "开发支出(元)",
                "商誉(元)", "长期待摊费用(元)", "递延税款借项合计(元)", "其他长期资产(元)", "非流动资产合计(元)", "资产总计(元)",
                "短期借款(元)", "向中央银行借款(元)", "吸收存款及同业存放(元)", "拆入资金(元)", "交易性金融负债(元)", "应付票据(元)",
                "应付帐款(元)", "预收帐款(元)", "卖出回购金融资产款(元)", "应付手续费及佣金(元)", "应付职工薪酬(元)", "应交税金(元)",
                "应付利息(元)", "应付股利(元)", "其他应付款(元)", "应付分保账款(元)", "保险合同准备金(元)", "代理买卖证券款(元)",
                "代理承销证券款(元)", "一年内到期的长期负债(元)", "其他流动负债(元)", "流动负债合计(元)", "长期借款(元)", "应付债券(元)",
                "长期应付款(元)", "专项应付款(元)", "预计负债(元)", "递延税款贷项合计(元)", "其他长期负债(元)", "长期负债合计(元)",
                "负债合计(元)", "股本(元)", "资本公积(元)", "库存股(元)", "盈余公积(元)", "一般风险准备(元)", "未分配利润(元)",
                "外币报表折算差额(元)", "归属于母公司所有者权益合计(元)", "少数股东权益(元)", "股东权益合计(元)", "负债和股东权益合计(元)")
# 利润表
profit = ("营业总收入(元)", "营业收入(元)", "金融资产利息收入(元)", "已赚保费(元)", "手续费及佣金收入(元)", "营业总成本(元)",
          "营业成本(元)", "金融资产利息支出(元)", "手续费及佣金支出(元)", "退保金(元)", "赔付支出净额(元)", "提取保险合同准备金净额(元)",
          "保单红利支出(元)", "分保费用(元)", "营业税金及附加(元)", "销售费用(元)", "管理费用(元)", "财务费用(元)", "资产减值损失(元)",
          "公允价值变动收益(元)", "投资收益(元)", "对联营企业和合营企业的投资收益(元)", "汇兑收益(元)", "营业利润(元)", "营业外收入(元)",
          "营业外支出(元)", "非流动资产处置净损失(元)", "利润总额(元)", "所得税(元)", "净利润(元)", "归属于母公司所有者的净利润(元)",
          "少数股东损益(元)", "基本每股收益(元)", "稀释每股收益(元)")
# 现金流表
cash_stream = ("销售商品提供劳务收到的现金(元)", "客户存款和同业存放款项净增加额(元)", "向中央银行借款净增加额(元)",
               "向其他金融机构拆入资金净增加额(元)", "收到原保险合同保费取得的现金(元)", "收到再保险业务现金净额(元)",
               "保户储金及投资款净增加额(元)", "处置交易性金融资产净增加额(元)", "收取利息、手续费及佣金的现金(元)", "拆入资金净增加额(元)",
               "回购业务资金净增加额(元)", "收到的税费返还(元)", "收到的其他与经营活动有关的现金(元)", "经营活动现金流入小计(元)",
               "购买商品接受劳务支付的现金(元)", "客户贷款及垫款净增加额(元)", "存放中央银行和同业款项净增加额(元)",
               "支付原保险合同赔付款项的现金(元)", "支付利息、手续费及佣金的现金(元)", "支付保单红利的现金(元)",
               "支付给职工以及为职工支付的现金(元)", "支付的各项税费(元)", "支付的其他与经营活动有关的现金(元)", "经营活动现金流出小计(元)",
               "经营活动现金流量净额(元)", "收回投资所收到的现金(元)", "取得投资收益所收到的现金(元)",
               "处置固定资产、无形资产和其他长期资产而收回的现金(元)", "收回投资所收到的现金中的出售子公司收到的现金(元)",
               "收到的其他与投资活动有关的现金(元)", "投资活动现金流入小计(元)", "购建固定资产、无形资产和其他长期资产所支付的现金(元)",
               "投资所支付的现金(元)", "质押贷款净增加额(元)", "取得子公司及其他营业单位支付的现金净额(元)",
               "支付的其他与投资活动有关的现金(元)", "投资活动现金流出小计(元)", "投资活动产生的现金流量净额(元)", "吸收投资所收到的现金(元)",
               "吸收投资所收到的现金中的子公司吸收少数股东权益性投资收到的现金(元)", "借款所收到的现金(元)", "发行债券所收到的现金(元)",
               "收到其他与筹资活动有关的现金(元)", "筹资活动现金流入小计(元)", "偿还债务所支付的现金(元)",
               "分配股利利润或偿付利息所支付的现金(元)", "分配股利利润或偿付利息所支付的现金中的支付少数股东的股利(元)",
               "支付的其他与筹资活动有关的现金(元)", "筹资活动现金流出小计(元)", "筹资活动产生的现金流量净额(元)", "汇率变动对现金的影响(元)",
               "现金及现金等价物净增加额(元)", "现金及现金等价物余额(元)")


# 获取批发及零售行业上市公司股票代码和简称
def get_resale_company():
    company_info = []
    req = requests.get("http://listxbrl.sse.com.cn/hybj/listCompany.do?csrcCode=F&csrcGreatCode=")
    resale_data_json = json.loads(req.text)
    for item in resale_data_json["dataList"]:
        companyCode = item["companyCode"]
        companyAbbr = item["companyAbbr"]
        company_info.append({"companyCode": companyCode, "companyAbbr": companyAbbr})
    company_info.remove({"companyCode": "601086", "companyAbbr": "国芳集团"})
    company_info.remove({"companyCode": "601366", "companyAbbr": "利群股份"})
    company_info.remove({"companyCode": "603233", "companyAbbr": "大参林"})
    company_info.remove({"companyCode": "603970", "companyAbbr": "中农立华"})

    return company_info


# 获取上市公司数据
def get_company_date(stock_id, companyAbbr, tuple_date, url):
    '''
    :param stock_id: 公司代码
    :param companyAbbr: 公司名称
    :param tuple_date: 表行标签元组
    :param url: 每张基本表的链接
    :return:
    '''
    num = 0
    if num >= 3:
        return None
    params = {"report_year": "2016",
              "stock_id": stock_id,
              "report_period_id": "5000",
              }
    req = requests.get(url, params, allow_redirects=False)
    time.sleep(1)
    # 创建数组保存表中的数值
    date = []
    if req.status_code == 200:
        date_json = json.loads(req.text)
        # 获取公司数据表的列标签
        year_columns = date_json["columns"][0]
        # 获取公司数据表的数值
        rows_num = date_json["rows"]
        index = 0
        for line in rows_num:
            if "value0" in line.keys():
                value0 = str(line["value0"]).replace("<div style='text-align: left;'>", "").replace("</div>", "")
            else:
                value0 = "-"
            if "value1" in line.keys():
                value1 = str(line["value1"]).replace("<div style='text-align: left;'>", "").replace("</div>", "")
            else:
                value1 = "-"

            if "value2" in line.keys():
                value2 = str(line["value2"]).replace("<div style='text-align: left;'>", "").replace("</div>", "")
            else:
                value2 = "-"
            if "value3" in line.keys():
                value3 = str(line["value3"]).replace("<div style='text-align: left;'>", "").replace("</div>", "")
            else:
                value3 = "-"
            if "value4" in line.keys():
                value4 = str(line["value4"]).replace("<div style='text-align: left;'>", "").replace("</div>", "")
            else:
                value4 = "-"
            date0 = [companyAbbr, stock_id, tuple_date[index], year_columns[0]["title"], value0]
            date1 = [companyAbbr, stock_id, tuple_date[index], year_columns[1]["title"], value1]
            date2 = [companyAbbr, stock_id, tuple_date[index], year_columns[2]["title"], value2]
            date3 = [companyAbbr, stock_id, tuple_date[index], year_columns[3]["title"], value3]
            date4 = [companyAbbr, stock_id, tuple_date[index], year_columns[4]["title"], value4]
            date.append(date1)
            date.append(date0)
            date.append(date3)
            date.append(date2)
            date.append(date4)
            index += 1
    else:
        num += 1
        return get_company_date(stock_id, companyAbbr, tuple_date, url)
    return date


def main():
    with open(r"C:\Users\chen\Desktop\新建 Microsoft Excel 工作表.csv", "w+", newline="") as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(["companyAbbr", "stock_id", "feature", "year", "value"])
        suggestData = get_resale_company()
        companyInfoUrl = "http://listxbrl.sse.com.cn/companyInfo/showmap.do"
        capitalUrl = "http://listxbrl.sse.com.cn/capital/showmap.do?"
        showTopTenMapUrl = "http://listxbrl.sse.com.cn/companyInfo/showTopTenMap.do"
        balanceUrl = "http://listxbrl.sse.com.cn/companyInfo/showBalance.do"
        profitUrl = "http://listxbrl.sse.com.cn/profit/showmap.do"
        cashUrl = "http://listxbrl.sse.com.cn/cash/showmap.do"
        count = 0
        for item in suggestData:
            # 基本信息表
            compInfoDate = get_company_date(item["companyCode"], item["companyAbbr"], basic_info, companyInfoUrl)
            # 股本结构表
            capitalDate = get_company_date(item["companyCode"], item["companyAbbr"], stock_structure, capitalUrl)
            # 前十大股东表
            topTenMapDate = get_company_date(item["companyCode"], item["companyAbbr"], top_ten_shareholder,
                                             showTopTenMapUrl)

            # 资产负债表
            balanceDate = get_company_date(item["companyCode"], item["companyAbbr"], assert_debts, balanceUrl)
            # 利润表
            profitDate = get_company_date(item["companyCode"], item["companyAbbr"], profit, profitUrl)
            # 现金流量表
            cashDate = get_company_date(item["companyCode"], item["companyAbbr"], cash_stream, cashUrl)
            for item in compInfoDate:
                writer.writerow([date for date in item])
            for item in capitalDate:
                writer.writerow([date for date in item])
            for item in topTenMapDate:
                writer.writerow([date for date in item])
            for item in balanceDate:
                writer.writerow([date for date in item])
            for item in profitDate:
                writer.writerow([date for date in item])
            for item in cashDate:
                writer.writerow([date for date in item])
            count += 1
            print("第" + str(count) + "次写入成功")


if __name__ == '__main__':
    main()
