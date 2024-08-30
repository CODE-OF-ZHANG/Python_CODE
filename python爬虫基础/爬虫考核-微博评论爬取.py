# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 爬虫考核-微博评论爬取
# @Software: PyCharm
# @Date : 2024/4/3

"""
目标网站：https://weibo.com/
需求：在该平台，找评论超过100的任意动态，采集评论区的数据
采集字段：评论用户id+评论时间(需将时间戳转换为北京时间+评论内容+用户地点)
数据存储方案：csv、excel二者选一
"""
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pywin32

# 导包
import requests
import csv

# 目标url
url = 'https://weibo.com/ajax/statuses/buildComments?is_reload=1&id=5019069826991257&is_show_bulletin=2&is_mix=0&count=10&uid=1246130430&fetch_level=0&locale=zh-CN'
# 伪装
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'Cookie': 'SINAGLOBAL=7297477823795.157.1708350962878; UOR=,,ask.csdn.net; XSRF-TOKEN=ziIoYMTVcYhbrFlERVv2udg-; PC_TOKEN=35a1c6f6b6; login_sid_t=38e022b42c9c55a3282c2edee71fc1ed; cross_origin_proto=SSL; WBStorage=267ec170|undefined; _s_tentry=-; Apache=9231893510781.572.1712153496489; ULV=1712153496491:4:1:1:9231893510781.572.1712153496489:1708670382600; SUB=_2AkMRUeyqf8NxqwFRmfoTzmzjbY9-yQ3EieKnDR1xJRMxHRl-yT9vqkEotRB6OtHCRbc-6YjPYUanqrgzXFt_TaDz7TMl; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WFdypB4Q6mvDHyFE9qKzjAk; WBPSESS=V0zdZ7jH8_6F0CA8c_ussdfqZTpvy6gNUyKs7KCsph-cRrOj5w6QyJ1jBKhIAzrVV7WNlzyQaOMw6kH-9ij4Hk5Y4UEpCa3UT27lt1CWshj36RW8Hjn9P2PJ27fHya7XG3bL77RMG3iw9hQrTkkXURIwgKEwUctciBZm_Fyogto=',
    'Referer': 'https://weibo.com/1246130430/O805MtkKd?ref=feedsdk'
}
# 发送请求, 获取响应
res = requests.get(url, headers=headers)

# print(res.text)
data = res.json()
# print(data)
user_list = []
for d in data['data']:
    dic = {}
    Id = d['id']  # id号
    dic['用户ID'] = Id
    concent = d['text_raw']  # 评论内容
    dic['评论内容'] = concent
    name = d['user']['screen_name']
    dic['用户名'] = name
    time = d['created_at']
    dic['时间'] = time
    place = d['source']
    dic['地点'] = place
    user_list.append(dic)
    # print(name, Id, time, concent, place)
# 数据保存
with open('微博评论.csv', 'w', encoding='utf-8-sig', newline='') as f:
    # 1. 创建对象
    writer = csv.DictWriter(f, fieldnames=('用户ID', '用户名', '评论内容', '时间', '地点'))
    # 2. 写入表头
    writer.writeheader()
    # 3. 写入数据
    writer.writerows(user_list)
