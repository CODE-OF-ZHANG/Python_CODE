# 导入模块
import requests
from bs4 import BeautifulSoup
# from comtypes.client import CreateObject
# from comtypes.gen import SpeechLib  # 导入 SpeechLib
import os

# 伪装
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}


# 获取网页源码
def get_html(url):
    res = requests.get(url, headers=head)
    # print(res.text)  # 打印查看网页源码
    return res.text


# 解析数据
def parse_html(html):
    soup = BeautifulSoup(html, 'lxml')  # 实例化对象
    divs = soup.find('div', class_='listmain')  # 寻找<div class="listmain"> 标签
    # print(divs)  # 打印目标div及其子标签
    dds = divs.find_all('dd')  # 通过div去寻找其子标签中所有的dd标签
    # print(dds[0])
    dds_del = dds.pop(10)
    for dd in dds:
        a = dd.find('a')
        title = a.string
        # print(title)
        href = 'https://www.bqgka.com' + a['href']
        # print(href)
        html = get_html(href)
        tag_concent = BeautifulSoup(html, 'lxml')
        p_tag = tag_concent.find('p', class_='readinline')
        # print(p_tag)
        div_tag = p_tag.parent
        # print(div_tag)
        concent = div_tag.text.replace('<br>', '\n').strip()
        # print(concent)
        save_data(title, concent)


# 保存数据
def save_data(title, concent):
    path = '飞刀弱？可知小李飞刀，例无虚发'
    if not os.path.exists(path):
        os.mkdir(path)
    with open(f'{path}\\{title}.txt', 'w', encoding='utf-8') as f:
        f.write(concent)
    print(f'{title}下载成功')


# 主函数
def main():
    url = 'https://www.bqgka.com/book/170784/'
    html = get_html(url)
    parse_html(html)


main()
