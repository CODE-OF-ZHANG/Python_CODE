import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from chaojiying import Chaojiying_Client

driver = webdriver.Chrome()
driver.get('https://www.chaojiying.com/')
# driver.maximize_window()
# 点击登录
driver.find_element(By.CLASS_NAME, 'login').click()
# 输入账号密码
driver.find_element(By.ID, 'user').send_keys('15576806087')
driver.find_element(By.ID, 'pass').send_keys('s15576806087')
# 找到验证码图片
cjy_img = driver.find_element(By.XPATH, '//*[@id="userone"]/section/form/div[3]/div/img')
# 截图
cjy_img.screenshot('cjy.png')
time.sleep(1)
# 识别验证码
chaojiying = Chaojiying_Client('15576806087', 's15576806087', '962830')
im = open('cjy.png', 'rb').read()
yzm = chaojiying.PostPic(im, 1004)['pic_str']
print(yzm)
time.sleep(1)
# 输入验证码
driver.find_element(By.ID, 'auth').send_keys(yzm)
driver.find_element(By.XPATH, '//*[@id="userone"]/section/form/div[6]/button').click()
