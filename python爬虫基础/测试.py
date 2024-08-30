"""
# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 测试
# @Software: PyCharm
# @Date : 2024/1/26 
"""

# import requests
# from bs4 import BeautifulSoup
# import time
#
# url = 'https://s.weibo.com/weibo?q=%E6%96%87%E6%97%85&xsort=hot&suball=1&Refer=g&page=1'
# head = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     'Accept-Encoding': 'gzip, deflate, br, zstd',
#     'Accept-Language': 'zh-CN,zh;q=0.9',
#     'Cache-Control': 'max-age=0',
#     'Cookie': 'SINAGLOBAL=7297477823795.157.1708350962878; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhjUz6rHqZuLkcprlFNCNA85JpX5o275NHD95QNe0nfS05EeoBpWs4Dqcj3i--RiK.ciKnXi--ciKn0iKnfi--fiKnfiKnRi--ci-20i-88Hsv_dPLk; ALF=1711176062; SUB=_2A25I0pzQDeRhGeFN41cW8CzOzz2IHXVrkZAYrDV8PUNbktANLRXzkW9NQ9MD_m3i1KGlYrt5oKkOLKuI1qGeO13z; _s_tentry=ask.csdn.net; UOR=,,ask.csdn.net; Apache=3214651599043.6406.1708670382565; ULV=1708670382600:3:3:3:3214651599043.6406.1708670382565:1708583641585',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
# }
# response = requests.get(url, headers=head)
# html = response.text
# # print(html)
# soup = BeautifulSoup(html, 'html.parser')
# # 提取微博内容和点赞数
# weibo_list = soup.select('.card-wrap .card')
# for weibo in weibo_list:
#     content_node = weibo.select_one('.txt')
#     if content_node:
#         content = content_node.text.strip()
#     else:
#         content = 'No content available'
#
#     like_num_node = weibo.select_one('.card-act span:nth-of-type(3)')
#     like_num = like_num_node.text.strip() if like_num_node else '0'
#
#     print(content, like_num)
# max_page = 100  # 爬取的最大页数
# for page in range(1, max_page+1):
#     url = 'https://s.weibo.com/weibo?q=%E6%96%87%E6%97%85&xsort=hot&suball=1&Refer=g&page={}'.format(page)
#     response = requests.get(url)
#     html = response.text
#     soup = BeautifulSoup(html, 'html.parser')
#
#     weibo_list = soup.select('.card-wrap .card')
#     for weibo in weibo_list:
#         p_tags = soup.select('p.txt')
#         second_p_tag = p_tags[1]
#         content = second_p_tag.text.strip()
#         # content = result.replace(f'@白鹿视频 L白鹿视频的微博视频 收起d', '')
#         like_num = weibo.select_one('.card-act span:nth-of-type(3)').text.strip()
#         print(content, like_num)
#
#     # 每爬取一页，暂停一段时间，防止被反爬虫
#     time.sleep(1)

# import requests
# from bs4 import BeautifulSoup
# import time
#
# max_page = 100
# base_url = 'https://s.weibo.com/weibo?q=%E6%96%87%E6%97%85&xsort=hot&suball=1&Refer=g&page={}'
# head = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     'Accept-Encoding': 'gzip, deflate, br, zstd',
#     'Accept-Language': 'zh-CN,zh;q=0.9',
#     'Cache-Control': 'max-age=0',
#     'Cookie': 'SINAGLOBAL=7297477823795.157.1708350962878; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhjUz6rHqZuLkcprlFNCNA85JpX5o275NHD95QNe0nfS05EeoBpWs4Dqcj3i--RiK.ciKnXi--ciKn0iKnfi--fiKnfiKnRi--ci-20i-88Hsv_dPLk; ALF=1711176062; SUB=_2A25I0pzQDeRhGeFN41cW8CzOzz2IHXVrkZAYrDV8PUNbktANLRXzkW9NQ9MD_m3i1KGlYrt5oKkOLKuI1qGeO13z; _s_tentry=ask.csdn.net; UOR=,,ask.csdn.net; Apache=3214651599043.6406.1708670382565; ULV=1708670382600:3:3:3:3214651599043.6406.1708670382565:1708583641585',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
# }
#
# for page in range(1, max_page + 1):
#     url = base_url.format(page)
#     response = requests.get(url, headers=head)
#     html = response.text
#     soup = BeautifulSoup(html, 'html.parser')
#
#     weibo_cards = soup.select('.card-wrap .card')
#     for card in weibo_cards:
#         p_tags = soup.select('p.txt')
#         second_p_tag = p_tags[1]
#         result = second_p_tag.text.strip()
#         content = result.replace(f'@白鹿视频 L白鹿视频的微博视频 收起d', '')
#         like_num_node = card.select_one('.card-act span:nth-of-type(2)')
#         # like_num_node = card.select_one('.card-act span:nth-of-type(2)')
#         like_num = like_num_node.text.strip() if like_num_node else '0'
#
#         print("微博内容:", content)
#         print("点赞数:", like_num)
#         print('-' * 50)
#
#     # 每爬取一页，暂停一段时间，防止被反爬虫
#     time.sleep(1)
# from pywin32 import winsounde
import requests
url = 'https://movie.douban.com/top250'
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
response = requests.get(url, headers=head)
print(response.text)
