import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BiliBili:
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
        img_location = div_img.location
        img_size = div_img.size
        print(img_location, img_size)
        x1, y1 = int(img_location['x']), int(img_location['y'])
        x2, y2 = x1 + img_size['width'], y1 + img_size['height']
        pass

    def run(self):
        self.login()
        self.login_image()
        self.save_image()
        # 在这里可以添加


if __name__ == '__main__':
    bilibili = BiliBili('123165', '346584')
    bilibili.run()
