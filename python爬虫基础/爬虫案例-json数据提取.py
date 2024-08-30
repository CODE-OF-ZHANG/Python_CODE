"""
# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 爬虫案例-json数据提取
# @Software: PyCharm
# @Date : 2024/1/26 
"""

"""
目标网站: http://www.whggzy.com/
需求: 获取前五页的标题跟时间
思路:
1.先把第一页的数据获取下来
2.后面几页的数据通过循环重复获取就可以
目标url: http://www.whggzy.com/portal/category
"""

# 导入模块
import requests
import time

# 目标url
url = 'http://www.whggzy.com/portal/category'
# 伪装请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}
pages = int(input('请输入你要爬取的页数:'))
for page in range(1, pages+1):
    # 请求载荷
    load = {
        "pageNo": page,
        "pageSize": 15,
        "categoryCode": "GovernmentProcurement",
        "_t": 1709006601000
    }

    # 发送请求，获取响应
    res = requests.post(url, headers=headers, json=load)

    data = res.json()['result']['data']['data']
    # 循环遍历
    for d in data:
        # print(d)
        title = d['title']
        # print(title)
        # 获取时间戳
        publishDate = d['publishDate']
        # print(publishDate)
        # 将时间戳转化为日期
        timeArray = time.localtime(publishDate / 1000)
        otherStyleTime = time.strftime('%Y-%m-%d %H:%M:%S', timeArray)
        print(title, otherStyleTime)
    print(f'第{page}页爬取完成', '-'*50)
