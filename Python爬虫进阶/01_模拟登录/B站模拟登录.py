import time

from PIL import Image
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from chaojiying import Chaojiying_Client
# pip install pillow -i https://pypi.tuna.tsinghua.edu.cn/simple


class BiliBili(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://www.bilibili.com/')
        self.wait = WebDriverWait(self.driver, 2)

    def login(self):
        # 点击登录按钮
        self.driver.find_element(By.CLASS_NAME, 'header-login-entry').click()
        # 显示等待
        self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, 'bili-mini-content-wp'))
        )
        print('登录窗口加载完成')

    def login_image(self):
        self.driver.find_element(By.XPATH, '/html/body/div[4]/div/div[4]/div[2]/form/div[1]/input').send_keys(
            self.username)
        self.driver.find_element(By.XPATH, '/html/body/div[4]/div/div[4]/div[2]/form/div[3]/input').send_keys(
            self.password)
        self.driver.find_element(By.CLASS_NAME, 'btn_primary ').click()
        # 显示等待
        self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, 'geetest_widget'))
        )

    def save_image(self):
        time.sleep(2)
        self.driver.save_screenshot('back_img.png')
        print('验证窗口加载完成')
        div_img = self.driver.find_element(By.CLASS_NAME, 'geetest_panel_next')
        print(div_img.location)
        img_location = div_img.location
        x1, y1 = img_location['x'], img_location['y']
        img_size = div_img.size
        print(img_size)
        x2, y2 = x1 + img_size['width'], y1 + img_size['height']
        back_img = Image.open('back_img.png')
        img = back_img.crop((x1, y1, x2, y2))
        img.save('yzm.png')
        return div_img

    def clock_font(self, dic, yzm_img):
        for x, y in dic.items():
            action = ActionChains(self.driver)
            action.move_to_element_with_offset(yzm_img, int(x), int(y)).click().perform()
        self.driver.find_element(By.CLASS_NAME, 'geetest_commit_tip').click()

    def run(self):
        self.login()
        self.login_image()
        yzm_img = self.save_image()
        chaojiying = Chaojiying_Client('15576806087', 's15576806087', '962830')
        im = open('yzm.png', 'rb').read()
        yzm = chaojiying.PostPic(im, 9004)['pic_str']
        lic_list = yzm.split('|')
        dic = {}
        for i in lic_list:
            s = i.split(',')
            dic[s[0]] = s[1]
        self.clock_font(dic, yzm_img)


if __name__ == '__main__':
    bilibili = BiliBili('123165', '346584')
    bilibili.run()
