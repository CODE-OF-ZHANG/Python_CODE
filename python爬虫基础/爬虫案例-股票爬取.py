# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 爬虫案例-股票爬取
# @Software: PyCharm
# @Date : 2024/4/23

import requests
import re
import pandas  # pip install pandas

mylist = []
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0',
    'Cookie': 'Hm_lvt_45db753385e6d769706e10062e3d6453=1713627708; __gads=ID=eb3b22ef856f3a03:T=1713627706:RT=1713634521:S=ALNI_MYpG4KEiVqehyQpAdMuLjY99IyH-Q; __gpi=UID=00000df448ad55f0:T=1713627706:RT=1713634521:S=ALNI_MZOjUJ7BNGwksg5bwsfYC0LqYT8Ww; __eoi=ID=4e3103c2faa50971:T=1713627706:RT=1713634521:S=AA-AfjalGW8Ijjyq4zLmBnIW8lSX; Hm_lpvt_45db753385e6d769706e10062e3d6453=1713634604'
}
page = 1
while True:
    url = f'https://4.push2.eastmoney.com/api/qt/clist/get?cb=jQuery1124010309705084016807_1713871270262&pn={page}&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&wbp2u=|0|0|0|web&fid=f3&fs=m:0+t:6,m:0+t:80,m:1+t:2,m:1+t:23,m:0+t:81+s:2048&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152&_=1713871270263'
    res = requests.get(url, headers=headers)
    code = re.findall('"f12":"(.*?)","f13"', res.text)
    if not code:
        break
    name_g = re.findall('"f14":"(.*?)","f15"', res.text)
    new_price = re.findall('"f2":(.*?),"f3"', res.text)
    quote_p = re.findall('"f3":(.*?),"f4"', res.text)
    for i in range(len(name_g)):
        print(code[i], name_g[i], new_price[i], quote_p[i])
        list = [code[i], name_g[i], new_price[i], quote_p[i]]
        mylist.append(list)
    page += 1
data = pandas.DataFrame(data=mylist)
data.to_excel('股票.xlsx', index=False, header=['股票代码', '企业名称', '最新价格', '涨跌幅'])
