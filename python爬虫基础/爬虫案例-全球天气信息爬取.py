# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 爬虫案例-全球天气信息爬取
# @Software: PyCharm
# @Date : 2024/5/6

import requests
from bs4 import BeautifulSoup
import csv


list_data = []
# 获取网页源码
def get_html(url):
    html = requests.get(url)
    html.encoding = 'utf-8'
    # print(html.text)
    return html.text


# 解析数据
def parse_html(html):
    # 创建对象
    soup = BeautifulSoup(html, 'html5lib')  # 将lxml换成html5lib
    conMidtab = soup.find('div', class_="conMidtab")
    tables = conMidtab.find_all('table')
    # print(tables)
    for table in tables:
        trs = table.find_all('tr')[2:]
        # print(trs)
        for index, tr in enumerate(trs):
            dic = {}
            tds = tr.find_all('td')
            # print(tds)
            if index == 0:  # 第一个城市取第二个td标签
                city = list(tds[1].stripped_strings)[0]  # 城市
            else:  # 其余的取第一个td标签
                city = list(tds[0].stripped_strings)[0]  # 城市
            dic['城市'] = city
            temp = tds[-2].string  # 最低气温
            dic['最低气温'] = temp
            list_data.append(dic)


# 保存数据
def save_data():
    with open('全国天气.csv', 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=('城市', '最低气温'))
        writer.writeheader()
        writer.writerows(list_data)


# 主函数
def main():
    district = ['hb', 'db', 'hd', 'hz', 'hn', 'xb', 'xn', 'gat']
    # url = 'http://www.weather.com.cn/textFC/hz.shtml'
    # url = 'http://www.weather.com.cn/textFC/hb.shtml'
    for dist in district:
        url = f'http://www.weather.com.cn/textFC/{dist}.shtml'
        html = get_html(url)
        parse_html(html)
    save_data()  # 数据保存


main()


# # 获取网页源码
# def get_html(url):
#     html = requests.get(url)
#     html.encoding = 'utf-8'
#     # print(html.text)
#     return html.text
#
#
# # 解析数据
# def parse_html(html):
#     # 创建对象
#     soup = BeautifulSoup(html, 'lxml')
#     conMidtab = soup.find('div', class_="conMidtab")
#     tables = conMidtab.find_all('table')
#     # print(tables)
#     for table in tables:
#         trs = table.find_all('tr')[2:]
#         # print(trs)
#         for index, tr in enumerate(trs):
#             tds = tr.find_all('td')
#             # print(tds)
#             city = list(tds[1].stripped_strings)[0]  # 城市
#             temp = tds[-2].string  # 最低气温
#             print(city, temp)
#
#         break
#
# # 保存数据
# def save_data():
#     pass
#
#
# # 主函数
# def main():
#     url = 'http://www.weather.com.cn/textFC/hz.shtml'
#     html = get_html(url)
#     parse_html(html)
# main()