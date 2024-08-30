# 导入模块
import requests
from bs4 import BeautifulSoup
from win32com.client import Dispatch
import os
import re

# 请求头
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}


# 获取网页
def get_html(url):
    res = requests.get(url, headers=head)
    return res.text


# 保存数据
def save_data(title, concent):
    path = '别这么对我'
    if not os.path.exists(path):
        os.mkdir(path)
    with open(f'{path}/{title}.txt', 'w', encoding='utf-8') as f:
        f.write(concent)
    print(f'{title}章节爬取成功-----------------------------------------')


# 解析数据
def parse_html(html):
    soup = BeautifulSoup(html, 'lxml')
    # 解析目录及其小说详情页
    tag_div = soup.find('div', class_='listmain')
    tag_dd = tag_div.find_all('dd')
    for tag in tag_dd:
        tag_a = tag.find('a')
        title = tag_a.string
        if title == '<<---展开全部章节--->>':
            continue
        title = re.sub(r'[?*:"\/|]', '', title)
        href = 'https://www.3bqg.cc' + tag_a.get('href')
        html = get_html(href)
        soup1 = BeautifulSoup(html, 'lxml')
        tag_div1 = soup1.find('div', id='chaptercontent')
        data = list(tag_div1.stripped_strings)
        content = '\n  '.join(data)
        save_data(title, content)


# def voice_reading():
#     path = r'D:\python文件\python爬虫基础\别这么对我'
#     dirs = os.listdir(path)
#     for file in dirs:
#         print(file)
#         with open(f'{path}\\{file}', 'r', encoding='utf-8') as f:
#             data = f.read()
#             # print(data)
#             speaker = Dispatch('SAPI.SpVoice')
#             speaker.Speak(data)
#             del speaker


# 主函数
def main():
    url = 'https://www.3bqg.cc/book/3782/'
    html = get_html(url)
    parse_html(html)
    # voice_reading()


main()






