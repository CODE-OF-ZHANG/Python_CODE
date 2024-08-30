# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 爬虫练习-VIP咕咪音乐爬取
# @Software: PyCharm
# @Date : 2024/8/9

import requests
import re
import os

headers = {
    'channel': '0140210'
}

song_name = input('请输入歌曲名: ')
url = f'https://c.musicapp.migu.cn/v1.0/content/search_all.do?text={song_name}&pageNo=1&pageSize=20&isCopyright=1&sort=1&searchSwitch=%7B%22song%22%3A1%2C%22album%22%3A0%2C%22singer%22%3A0%2C%22tagSong%22%3A1%2C%22mvSong%22%3A0%2C%22bestShow%22%3A1%7D'

res = requests.get(url)
# print(res.text)

copyrightId = re.findall('"copyrightId":"(.*?)",', res.text)[0]
contentId = re.findall('"contentId":"(.*?)",', res.text)[0]
albumId = re.findall('"albums":\[{"id":"(.*?)",', res.text)[0]
# print(albumId)

url2 = f'https://c.musicapp.migu.cn/MIGUM3.0/strategy/listen-url/v2.3?copyrightId={copyrightId}&contentId={contentId}&resourceType=2&albumId={albumId}&netType=01&toneFlag=PQ'

res2 = requests.get(url2, headers=headers)

song_url = re.findall('"url":"(.*?)",', res2.text)[0]
res3 = requests.get(song_url)

path = 'music'
if not os.path.exists(path):
    os.mkdir(path)
with open(f'music/{song_name}.mp3', 'wb') as f:
    f.write(res3.content)


