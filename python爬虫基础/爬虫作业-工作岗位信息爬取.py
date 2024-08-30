"""
# -*- coding: utf-8 -*-
# @Author : ZX
# @File : 爬虫作业-工作岗位信息爬取
# @Software: PyCharm
# @Date : 2024/1/26 
"""

"""
目标网站: https://www.liepin.com/zhaopin/?city=410&dq=410&pubTime=&currentPage=0&pageSize=40&key=python&suggestTag=&workYearCode=&compId=&compName=&compTag=&industry=&salary=&jobKind=&compScale=&compKind=&compStage=&eduLevel=&otherCity=&sfrom=search_job_pc&ckId=hwmufbahh4eacxrzevqwbxwfh36ui9d9&scene=input&skId=hwmufbahh4eacxrzevqwbxwfh36ui9d9&fkId=hwmufbahh4eacxrzevqwbxwfh36ui9d9&suggestId=
需求: 翻页爬取前3页的职位名称，薪资，公司名称
目标url: https://api-c.liepin.com/api/com.liepin.searchfront4c.pc-search-job
"""
# 导入模块
import requests

# 目标url
url = 'https://api-c.liepin.com/api/com.liepin.searchfront4c.pc-search-job'

# 请求头信息
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'X-Client-Type': 'web',
    'X-Fscp-Bi-Stat': '{"location": "https://www.liepin.com/zhaopin/?city=410&dq=410&pubTime=&currentPage=0&pageSize=40&key=python&suggestTag=&workYearCode=&compId=&compName=&compTag=&industry=&salary=&jobKind=&compScale=&compKind=&compStage=&eduLevel=&otherCity=&sfrom=search_job_pc&ckId=hwmufbahh4eacxrzevqwbxwfh36ui9d9&scene=input&skId=hwmufbahh4eacxrzevqwbxwfh36ui9d9&fkId=hwmufbahh4eacxrzevqwbxwfh36ui9d9&suggestId"}',
    'X-Fscp-Std-Info': '{"client_id": "40108"}',
    'X-Fscp-Trace-Id': '6b3c0cbf-8137-48e1-9627-32f958eceaa8',
    'X-Fscp-Version': '1.1',
    'X-Requested-With': 'XMLHttpRequest',
    'X-Xsrf-Token': '6gEp2kHpQW2D8PCrQol_zg'
}
pages = int(input('请输入你要爬取的页数:'))
for page in range(0, pages):
    # 载荷信息
    load = {"data": {
        "mainSearchPcConditionForm": {"city": "410", "dq": "410", "pubTime": "", "currentPage": page, "pageSize": 40,
                                      "key": "python", "suggestTag": "", "workYearCode": "", "compId": "",
                                      "compName": "",
                                      "compTag": "", "industry": "", "salary": "", "jobKind": "", "compScale": "",
                                      "compKind": "", "compStage": "", "eduLevel": ""},
        "passThroughForm": {"scene": "input", "skId": "hwmufbahh4eacxrzevqwbxwfh36ui9d9",
                            "fkId": "hwmufbahh4eacxrzevqwbxwfh36ui9d9", "ckId": "txiqi2f0gxdtzk2rk253nfv77s104lyb"
                            }}}
    # 发送请求, 获取响应
    res = requests.post(url, headers=headers, json=load)
    result = res.json()['data']['data']['jobCardList']
    # print(result)
    for data in result:
        title = data['job']['title']
        salary = data['job']['salary']
        compName = data['comp']['compName']
        print(title, salary, compName)
    print(f'第{page + 1}页爬取完毕', '-' * 50)
