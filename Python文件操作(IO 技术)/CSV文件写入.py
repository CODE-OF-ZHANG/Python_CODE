"""
# -*- coding: utf-8 -*-
# @Author : ZX
# @File : CSV文件写入
# @Software: PyCharm
# @Date : 2024/1/26 
"""

import csv

headers = ['标题', '类型', '评分', '引言']
rows = [('当幸福来敲门', '剧情 传记 家庭', 9.2, '平民励志片。'),
        ('寻梦环游记', '喜剧 动画 奇幻 音乐', 9.1, '死亡不是真的逝去，遗忘才是永恒的消亡。'),
        ('末代皇帝', '剧情 传记 历史', 9.3, '“不要跟我比惨，我比你更惨”再适合这部电影不过了。')]
with open('豆瓣.csv', 'w', encoding='utf-8', newline='') as f:
    write = csv.writer(f)
    write.writerow(headers)
    write.writerows(rows)
