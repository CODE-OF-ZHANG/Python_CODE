# 导入模块
import requests
import re
import json
import subprocess  # 执行构建好的命令

# 伪装
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
# 目标网站
url = 'https://www.bilibili.com/video/BV1Za4y1175i/?spm_id_from=333.1007.tianma.8-3-29.click&vd_source=d7e63ade2b80393846ef5a7ac06a47cf'
# 发送请求，获取响应
res = requests.get(url, headers=head)
# 打印响应内容，即源码
html = res.text
# 利用正则提取标题
title = re.findall(r'<title data-vue-meta="true">(.*?)_哔哩哔哩_bilibili</title>', html)[0]
# print(title)
# 利用正则提取json数据
content = re.findall(r'<script>window.__playinfo__=(.*?)</script>', html, re.S)[0]
# print(type(content))  # <class 'str'>
# print(content)
json_data = json.loads(content)
# 通过键值对提取视频和音频链接
video_url = json_data['data']['dash']['video'][0]['baseUrl']
audio_url = json_data['data']['dash']['audio'][0]['baseUrl']

# 打印视频和音频链接
# print(video_url)
# print(audio_url)

# 向目标url发起请求，获取响应内容
res1 = requests.get(video_url, headers=head)
res2 = requests.get(audio_url, headers=head)

# 保存视频和音频
with open('video.mp4', 'wb') as f:
    f.write(res1.content)
with open('audio.mp3', 'wb') as f:
    f.write(res2.content)

# 合并食品与音频
results = 'ffmpeg -i "video.mp4" -i "audio.mp3" -c:v copy -c:a aac -strict experimental B站视频.mp4'
subprocess.run(results, shell=True)
