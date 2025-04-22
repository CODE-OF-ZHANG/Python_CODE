# -*- coding: utf-8 -*-
# @Author : ZX
# @File : steam
# @Software: PyCharm
# @Date : 2025/4/11

"""
爬虫思路:
  一、 获取目标url: https://store.steamchina.com/search/?sort_by=Reviews_DESC
  二、 获取网页源码 --> GetHtml(url)
      并将网页源码下载保存到本地
"""

# # 导入模块
# import time
# import csv
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
#
# # 目标url
# url = 'https://store.steamchina.com/search/?sort_by=Reviews_DESC'
#
# # 构造浏览器对象, 模拟浏览器发起HTTP请求
# driver = webdriver.Chrome()
#
# # 窗口最大化
# driver.maximize_window()
# driver.get(url)
#
# # 等待加载
# wait = WebDriverWait(driver, 2)
#
# # 网页滚动条滚动功能
# last_height = driver.execute_script("return document.body.scrollHeight")
#
# while True:
#     # 滚动到页面底部
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(2)  # 等待页面加载
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         break
#     last_height = new_height
#
# # 游戏主页URL地址
# game_links = []
# games = driver.find_elements(By.ID, "search_resultsRows")
# for game in games:
#     link_elements = game.find_elements(By.XPATH, '//div[@id="search_resultsRows"]/a')
#     for link in link_elements:
#         game_links.append(link.get_attribute('href'))
# # print(game_links)
#
# # 遍历游戏URL列表，依次发起HTTP请求，获取游戏详细数据
# game_data = []
# for link in game_links:
#     driver.get(link)
#     time.sleep(1)  # 等待页面加载
#     # 获取游戏名称
#     name = driver.find_element(By.ID, "appHubAppName").text
#     # 获取游戏价格
#     price = driver.find_element(By.CLASS_NAME, "game_purchase_price price").text
#     # 获取好评率
#     review_score = driver.find_element(By.XPATH, 'div[@class="summary column"]/span[1]').text
#     print(review_score)
#     break


import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

# 目标url
url = "https://store.steamchina.com/search/?sort_by=Reviews_DESC"

# 构造浏览器对象, 模拟浏览器发起HTTP请求
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

# 等待加载
wait = WebDriverWait(driver, 10)

# 网页滚动条滚动功能
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # 滚动到页面底部
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # 等待页面加载
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# 游戏主页URL地址
game_links = []
games = driver.find_elements(By.ID, "search_resultsRows")
for game in games:
    link_elements = game.find_elements(By.TAG_NAME, "a")
    for link in link_elements:
        game_links.append(link.get_attribute('href'))

# 遍历游戏URL列表，依次发起HTTP请求，获取游戏详细数据
game_data = []
num = 1
for link in game_links:
    driver.get(link)
    time.sleep(1)  # 等待页面加载

    # 获取游戏名称
    try:
        name = driver.find_element(By.ID, "appHubAppName").text
    except:
        name = "N/A"

    # 获取游戏价格
    try:
        price = driver.find_element(By.CSS_SELECTOR, ".game_purchase_price.price").text
    except:
        price = "N/A"

    # 获取好评率
    try:
        review_score = driver.find_element(By.XPATH, '//div[@class="summary column"]/span[1]').text
    except:
        review_score = "N/A"
    # print(review_score)

    game_data.append({
        "游戏名称": name,
        "价格": price,
        "好评率": review_score
    })
    num += 1
    if num == 25:
        break

# print(game_data)
# 保存数据到CSV文件
with open("steam_games.csv", 'w', newline='', encoding='utf-8-sig') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["游戏名称", "价格", "好评率"])
    writer.writeheader()
    for row in game_data:
        writer.writerow(row)

# 关闭浏览器
driver.quit()
