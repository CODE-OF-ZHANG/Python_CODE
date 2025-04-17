# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 湖南城市天气
# @Software: PyCharm
# @Date : 2025/3/21

"""
爬虫思路:
  一、 获取目标url: https://www.tianqihoubao.com/lishi/changsha.html
  二、 获取网页源码 --> GetHtml(url)
      并将网页源码下载保存到本地
       1. 请求方式: get
       2. 请求头: user-agent
       3. 数据解析: BeautifulSoup

  三、 解析数据 --> ParseHtml(html)
      获取所需的数据
  四、 保存数据 --> SaveData()
      将数据以xlsx格式的文件保存到本地
  五、 主函数 --> Main()
      代码的执行入口
"""

# 22智能2班 张旭 202201170248
# 导入模块
import csv
import requests
from bs4 import BeautifulSoup
import os

list_data = []


# 请求头信息
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
}

# 目标url
url = 'http://www.tianqihoubao.com/lishi/changsha.html'


# 获取网页源代码
def GetHtml(url, filename):
    html = requests.get(url, headers=headers).text
    # 查看是否可以获取网页源码
    # print(html)

    # 将网页源代码下载到本地
    with open(f'Weather/{filename}.txt', 'w', encoding='utf-8') as f:
        f.write(html)
    return html


# 统一链接格式
def unify_link_format(link):
    if not link.startswith('/lishi/'):
        if link.startswith('lishi/'):
            return '/' + link
        elif link.startswith('changsha/'):
            return '/lishi/' + link
    return link


# 数据解析
def GetContUrl():
    # 读取文件内容
    with open('changsha.txt', 'r', encoding='utf-8') as f:
        html = f.read()

    # 创建对象
    links = []
    month = 202400
    soup = BeautifulSoup(html, 'html5lib')
    BoxPcity = soup.find_all('div', class_="box pcity")[1]
    # print(BoxPcity)
    Tag_A = BoxPcity.find_all('a')
    for tag_a in Tag_A:
        links.append(tag_a.get('href'))
    unified_links = [unify_link_format(link) for link in links]
    for url in unified_links:
        concent_url = 'http://www.tianqihoubao.com' + url
        print(concent_url)
        GetHtml(concent_url, f'changsha{month + 1}')
        month += 1
    pass


# 解析数据
def PraseHtml():
    folder_path = "Weather"
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            file_path = os.path.join(folder_path, filename)
            # print(file_path)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                soup = BeautifulSoup(content, 'html5lib')
                div = soup.find('div', id="content")
                table = soup.find('table')
                # print(div)
                title = div.find('h1').string.strip()
                # dic["标题"] = title
                # print(title)
                trs = table.find_all('tr')[1:]
                # print(trs)
                for tr in trs:
                    dic = {}
                    # 日期
                    date = tr.find('td').string.strip()
                    # print(date)
                    dic["日期"] = date
                    # 天气状况(白天/夜间)
                    weather = tr.find_all('td')[1].string.replace(" ", "").replace("\n\n", "").strip()
                    # print(weather)
                    dic["天气状况(白天/夜间)"] = weather
                    # 最高气温/最低气温
                    temp = tr.find_all('td')[2].string.replace(" ", "").replace("\n\n", "").strip()
                    # print(temp)
                    dic["最高气温/最低气温"] = temp
                    # 风力风向(白天/夜间)
                    wind = tr.find_all('td')[3].string.replace(" ", "").replace("\n\n", "").strip()
                    # print(wind)
                    dic["风力风向(白天/夜间)"] = wind
                    list_data.append(dic)


# 保存数据
def SaveData():
    with open('ChangSha/Weather.csv', 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=("日期", "天气状况(白天/夜间)",
                                               "最高气温/最低气温", "风力风向(白天/夜间)"))
        writer.writeheader()
        writer.writerows(list_data)
    pass


# 主函数
def Main():
    # 获取网页源
    # GetHtml(url, 'changsha')

    # 获取2024季度天气链接
    # GetContUrl()

    # 解析数据
    PraseHtml()

    # 保存数据
    SaveData()
    # print(list_data)


if __name__ == '__main__':
    Main()
