# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 爬虫案例-ppt模版爬取
# @Software: PyCharm
# @Date : 2024/4/19

# import requests  # 导入请求模块
# import re  # 正则表达式
#
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
#     'cookie': 'FCNEC=%5B%5B%22AKsRol_C6bmMej_9vqqhsy9sL-tiIyPbe-L0yBrTrJTXfDzL7EH2IWzvrjb_zpZg5UfznCNBeNSxtppndiSauDFGhWKd9vXjJnLV1Q-eJ9OdBsrvQY0JtxwL_FsxE6B-5RsEd3kMmSOulzMacvy-Ie1o_GFdIs9zlg%3D%3D%22%5D%5D; Hm_lvt_45db753385e6d769706e10062e3d6453=1713525320; __gads=ID=06d2fe923c77cc34:T=1706871525:RT=1713525322:S=ALNI_Ma6lhTe9LPxvLrVcLxwVMj2TKhWxw; __gpi=UID=00000cf6df84694d:T=1706871525:RT=1713525322:S=ALNI_MbX5yOM6whvtGs537K4xOcw_dNPeA; __eoi=ID=ab3ac68fa5117054:T=1706871525:RT=1713525322:S=AA-Afjb4Zw9atcqDQFJAdRhfrfSV; Hm_lpvt_45db753385e6d769706e10062e3d6453=1713525412'}  # 伪装
#
# page = 1
# while True:
#     # 获取PPT模板首页的数据！
#     if page == 1:
#         url = 'https://www.ypppt.com/moban/'
#     else:
#         url = f'https://www.ypppt.com/moban/list-{page}.html'
#
#     res = requests.get(url, headers=headers)  # 请求网站 得到响应
#     if res.status_code == 404:  # 按
#         break
#     res.encoding = 'utf-8'  # 发现编码不对  改成万国码 utf-8
#
#     # 从得到的数据里面提取若干个id
#     id_list = re.findall('href="/article/.*?/(.*?).html"class="', res.text)
#
#     # 把这些id拼接在'https://www.ypppt.com/p/d.php?aid='的后面
#     for aid in id_list:
#         url1 = 'https://www.ypppt.com/p/d.php?aid=' + aid
#         # 请求具体的一个ppt下载页面的链接
#         res1 = requests.get(url1, headers=headers)
#
#         # 得到下载链接
#         ppt_name = re.findall('<title>(.*?) - 下载页</title>', res1.text)[0]
#         down_url = re.findall('<a href="(.*?)">下载地址1</a></li>', res1.text)[0]
#         if 'pan.baidu' in down_url:
#             continue
#         else:
#             suffix = down_url.split('.')[-1]  # 获取后缀
#         res2 = requests.get(down_url, headers=headers)
#         open(f'ppt模板/{ppt_name}-{aid}.{suffix}', 'wb').write(res2.content)  # 文件名.后缀名
#         print(f'已经下载到{ppt_name}-{aid}.{suffix}')
#     page += 1  # 爬完一页 page+=1


# 导入请求模块
import requests
import re
# 忽略警告
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

page = 1  # 页数, 从第一页开始
while True:
    if page == 1:
        # 第一页
        url = 'https://www.ypppt.com/moban/'
    else:
        # 从第二页开始
        url = f'https://www.ypppt.com/moban/list-{page}.html'
    # 请求网址获得响应
    res = requests.get(url, headers=headers, verify=False)
    # 提取数据
    res.encoding = 'utf-8'  # 编码改成utf-8
    # print(res.text)
    ppt_info = re.findall('href="/article/.*?/(.*?).html" class="p-title" target="_blank">(.*?)</a>', res.text)
    for i, title in ppt_info:
        # 构造新的链接
        url1 = 'https://www.ypppt.com/p/d.php?aid=' + i
        res1 = requests.get(url1, headers=headers, verify=False)
        # print(res1.text)
        # 提取数据
        down_url = re.findall('href="(.*?)">下载地址1</a>', res1.text)[0]
        if 'pan.baidu' in down_url:  # 百度网盘下载
            continue
        else:
            suffix = down_url.split('.')[-1]  # 获取后缀名
        res2 = requests.get(down_url, headers=headers, verify=False)
        open(f'PPT模版/{title}-{i}.{suffix}', 'wb').write(res2.content)
        print(f'已成功下载{title}-{i}.{suffix}')
    page += 1  # 爬完之后页数+1


# 第1页：https://www.ypppt.com/moban/
# 第2页：https://www.ypppt.com/moban/list-2.html
# 第3页：https://www.ypppt.com/moban/list-3.html
# 第4页：https://www.ypppt.com/moban/list-4.html
# ...

