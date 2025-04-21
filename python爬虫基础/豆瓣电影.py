# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 豆瓣电影
# @Software: PyCharm
# @Date : 2025/3/14

"""
需求: 爬取豆瓣5部及以上电影的影评, 影评发表时间, 影评人昵称, 影评标题, 影评全文链接, 影评评价回应(有用/没用/回应), 最后写入csv文件中
1. 获取目标url: https://movie.douban.com/
2. 请求头: user-agent
3. 请求方式: get
4. 数据解析: xpath
"""


# 导入模块
import requests
from lxml import etree
import csv
import os

# 请求头信息
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
}

# 电影列表url
movie_url = 'https://movie.douban.com/'

# 发送请求
movie_res = requests.get(movie_url, headers=headers)

# 查看状态码 --> 200
# print(movie_res.status_code)

# 获取网页源码
movie_html = movie_res.text

# 实例化etree对象
movie_tree = etree.HTML(movie_html)

# 获取电影链接
movie_links = movie_tree.xpath('//ul[@class="ui-slide-content"]/li[@class="ui-slide-item s"]')
# print(len(movie_links))

movie_links_list = []
movie_names = []

# 获取电影的标题和链接
for movie in movie_links:
    # 获取电影标题
    movie_title = movie.xpath('./ul/li[@class="title"]/a/text()')[0]
    # print(movie_title)
    movie_names.append(movie_title)

    # 获取电影链接
    movie_link = movie.xpath('./ul/li[@class="title"]/a/@href')[0]
    print(movie_link)

    # 将电影链接添加到电影列表中
    movie_links_list.append(movie_link)

# 去掉每个标题末尾的省略号
trimmed_titles = [title.rstrip('...') for title in movie_names]
trimmed_titles = [title.replace('：', '') if '：' in title else title for title in trimmed_titles]

print(movie_links_list)

# 创建一个目录来保存CSV文件
os.makedirs('movie_reviews', exist_ok=True)

for url, title in zip(movie_links_list, trimmed_titles):
    # 电影目标url
    # url = "https://movie.douban.com/subject/34780991/"

    # 发送请求
    res = requests.get(url, headers=headers)

    # 查看状态码 --> 200
    # print(res.status_code)

    # 获取网页源码
    html = res.text
    # print(html)

    # 实例化etree对象
    tree = etree.HTML(html)

    # 定位元素 --> 找到所有的<header class="main-hd">, 数据类型为list
    main_header = tree.xpath('//header[@class="main-hd"]')

    # 获取用户昵称、影评发表时间
    nicknames = []
    pub_times = []
    for header in main_header:
        try:
            nickname = header.xpath('./a[@class="name"]/text()')[0]
            nicknames.append(nickname)

            # 影评发表时间
            pub_time = header.xpath('./span[@class="main-meta"]/text()')[0]
            pub_times.append(pub_time)
        except IndexError:
            continue

    # 定位元素 --> 找到所有的<div class="main-bd">, 数据类型为list
    main_divs = tree.xpath('//div[@class="main-bd"]')

    # 获取影评、影评标题、影评全文链接、影评评价回应(有用/没用/回应)
    reviews = []
    reviews_titles = []
    review_links = []
    review_responses = []

    for div in main_divs:
        try:
            # 在<div class="main-bd">中寻找包含影评的子节点
            review_text = div.xpath('./div/div[@class="short-content"]/text()')
            # 过滤掉空字符串, 并去除前后空白字符
            review_text = [text.strip() for text in review_text if text.strip()]
            # 去除多余的括号
            review_text = [text.strip('()') for text in review_text]
            # 合并提取的影评内容
            review_text = ''.join(review_text)
            reviews.append(review_text)

            # 获取影评标题
            review_title = div.xpath('./h2/a/text()')[0]
            reviews_titles.append(review_title)

            # 获取影评全文链接
            review_link = div.xpath('./h2/a/@href')[0]
            review_links.append(review_link)

            # 获取影评评价回应(有用/没用/回应)
            review_response = div.xpath('./div[@class="action"]/a[@class="reply "]/text()')[0]
            review_responses.append(review_response)
        except IndexError:
            continue

    # 创建CSV文件
    csv_filename = f'movie_reviews/{title}.csv'
    with open(csv_filename, 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        # 写入表头
        writer.writerow(['影评人昵称', '影评发表时间', '影评标题', '影评内容', '影评全文链接', '影评评价回应'])
        # 写入数据
        for i in range(len(nicknames)):
            writer.writerow([
                nicknames[i],
                pub_times[i],
                reviews_titles[i],
                reviews[i],
                review_links[i],
                review_responses[i]
            ])

    print(f'已保存 {title} 的影评到 {csv_filename}')
