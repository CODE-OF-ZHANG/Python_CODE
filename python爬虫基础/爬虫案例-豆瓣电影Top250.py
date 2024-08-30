"""
# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 爬虫案例-豆瓣电影Top250
# @Software: PyCharm
# @Date : 2024/1/26 
"""

"""
目标网站: https://movie.douban.com/top250
需求: 爬取电影中文名、英文名、电影详情页链接、导演、主演、上映年份、国籍、类型、评分、评分人数, 并保存到csv文件当中
目标url: https://movie.douban.com/top250
"""


# 导入模块
import requests
from lxml import etree
import csv

# 请求头信息
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

moive_list = []

for page in range(1, 11):
    # 目标url
    url = f'https://movie.douban.com/top250?start={(page - 1) * 25}&filter='

    # 发送请求, 获取响应
    res = requests.get(url, headers=headers)
    # 打印响应信息
    # print(res.text)
    # 网页源码
    html = res.text
    # 实例化etree对象
    tree = etree.HTML(html)

    divs = tree.xpath('//div[@class="info"]')
    # print(divs)
    for div in divs:
        dic = {}
        title = div.xpath('./div[@class="hd"]/a/span[@class="title"]/text()')
        # 电影中文标题
        title_cn = ''.join(title).split('\xa0/\xa0')[0]
        dic['电影中文名'] = title_cn
        # 电影英文标题
        title_en = div.xpath('./div[@class="hd"]/a/span[2]/text()')[0].strip('\xa0/\xa0')
        dic['电影英文名'] = title_en
        # 电影详情页链接
        links = div.xpath('./div[@class="hd"]/a/@href')[0]
        dic['电影详情页链接'] = links
        # print(links)
        # 导演
        director = div.xpath('./div[@class="bd"]/p/text()')[0].strip().split('导演: ')[1].split('主演: ')[0]
        dic['导演'] = director
        # print(director)
        # 主演
        try:
            act = div.xpath('./div[@class="bd"]/p/text()')[0].strip().split('导演: ')[1].split('主演: ')[1]
            # print(act)
        except IndexError as e:
            print(end='')
        dic['主演'] = act
        # 上映年份
        Release_year = div.xpath('./div[@class="bd"]/p/text()')[1].strip().split('/')[0]
        # print(Release_year)
        dic['上映年份'] = Release_year
        # print(Release_year)
        # 国籍
        nationality = div.xpath('./div[@class="bd"]/p/text()')[1].strip().split('/')[1].strip()
        if len(nationality[0].encode('utf-8')) == 1:
            nationality = div.xpath('./div[@class="bd"]/p/text()')[1].strip().split('/')[2].strip()
        else:
            nationality = div.xpath('./div[@class="bd"]/p/text()')[1].strip().split('/')[1].strip()
        # print(nationality)
        dic['国籍'] = nationality
        # print(title_cn, nationality)
        # 类型
        genre = div.xpath('./div[@class="bd"]/p/text()')[1].strip().split('/')[2].strip()
        if len(div.xpath('./div[@class="bd"]/p/text()')[1].strip().split('/')[1].strip()[0].encode('utf-8')) == 1:
            genre = div.xpath('./div[@class="bd"]/p/text()')[1].strip().split('/')[3].strip()
        else:
            genre = div.xpath('./div[@class="bd"]/p/text()')[1].strip().split('/')[2].strip()
        dic['类型'] = genre
        # print(genre)
        # 评分
        score = div.xpath('./div[@class="bd"]/div/span[2]/text()')[0]
        dic['评分'] = score
        # print(score)
        # 评分人数
        num_score = div.xpath('./div[@class="bd"]/div/span[4]/text()')[0]
        dic['评分人数'] = num_score
        # print(dic)
        moive_list.append(dic)
        # print(len(moive_list))  # 检查数据是否全部爬取成功
    print(f'----------------------第{page}页爬取完成--------------------------------------')
print('-----------------------爬虫结束-------------------------------')
# 数据保存
with open('豆瓣电影Top250.csv', 'w', encoding='utf-8-sig', newline='') as f:
    # 1. 创建对象
    writer = csv.DictWriter(f, fieldnames=('电影中文名', '电影英文名', '电影详情页链接', '导演', '主演', '上映年份', '国籍', '类型', '评分', '评分人数'))
    # 2. 写入表头
    writer.writeheader()
    # 3. 写入数据
    writer.writerows(moive_list)
