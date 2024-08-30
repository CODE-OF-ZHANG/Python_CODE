"""
# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 爬虫考核-房源信息爬取
# @Software: PyCharm
# @Date : 2024/1/26

目标网站：https://sh.58.com/ershoufang/
需求：获取房源标题，类型，面积，建造时间，地址，价格
数据存储方案：csv、excel二者选一
"""


import requests
import re
from lxml import etree


url = 'https://sh.58.com/ershoufang/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}
res = requests.get(url, headers=headers)

# print(res.text)
html = res.text
title_list = re.findall('class="property-content-title-name" style="max-width:467px;" data-v-51040db9>(.*?)</h3>', html)
# data_list = re.findall('<span data-v-51040db9>(.*?)</span>', html)





