import re

import requests
from bs4 import BeautifulSoup
from win32com.client import Dispatch
import os

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
}


class Novel_crawling(object):
    # 获取源码
    def get_html(self, url):
        res = requests.get(url, headers=headers)
        # print(res.text)
        return res.text

    # 数据解析
    def data_parsing(self, html):
        soup = BeautifulSoup(html, 'lxml')
        div = soup.find('div', class_='listmain')
        # print(div)
        for dd in div.find_all('dd')[6:]:
            title = dd.find('a').string
            if '<<---展开全部章节--->>' in title:
                continue
            title = re.sub(r'[?*:"/|]', '', title)
            link = 'https://www.3bqg.cc/' + dd.find('a').get('href')
            # print(title, link)
            html1 = self.get_html(link)
            soup1 = BeautifulSoup(html1, 'lxml')
            div1 = soup1.find('div', id='chaptercontent')
            # print(div1)
            data = div1.stripped_strings
            content = '  \n'.join(data)
            # print(content)
            self.save_data(title, content)

    # 数据保存
    def save_data(self, title, content):
        path = '别这么对我'
        if not os.path.exists(path):
            os.mkdir(path)
        with open(f'{path}/{title}.txt', 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'{title}章节爬取成功-----------------------------------------')

    def voice_reading(self):
        path = r'D:\python文件\python爬虫基础\别这么对我'
        dirs = os.listdir(path)
        for file in dirs:
            print(file)
            with open(f'{path}\\{file}', 'r', encoding='utf-8') as f:
                data = f.read()
                print(data)
                speaker = Dispatch('SAPI.SpVoice')
                speaker.Speak(data)
                del speaker

    # 主方法
    def main(self):
        html = self.get_html('https://www.3bqg.cc/book/3782/')
        self.data_parsing(html)
        self.voice_reading()


if __name__ == '__main__':
    novel = Novel_crawling()
    novel.main()
