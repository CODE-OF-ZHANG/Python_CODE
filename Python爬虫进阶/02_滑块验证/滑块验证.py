import random
import time

# 导入selenium
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
# 显示等待
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 鼠标行为链
from selenium.webdriver import ActionChains
from PIL import Image


class Slider(object):
    def __init__(self):
        # 加载驱动
        self.driver = webdriver.Chrome()
        # 最大化窗口
        self.driver.maximize_window()
        # 显示等待
        self.wait = WebDriverWait(self.driver, 5)
        # 目标url
        self.url = 'https://www.geetest.com/demo/slide-float.html'
        # 缺口图片
        self.gap_img = 'gap_img.png'
        # 完整图片
        self.full_img = 'full_img.png'

    # 保存图片
    def login_img(self):
        # 加载网页
        self.driver.get(self.url)
        # 显示等待文字
        self.wait.until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, 'geetest_radar_tip_content'), '点击按钮进行验证')
        )
        # 点击元素
        self.driver.find_element(By.CLASS_NAME, 'geetest_radar_tip_content').click()
        # 显示等待, 等待滑块元素出现
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="geetest_canvas_img geetest_absolute"]'))
        )
        # 执行js代码, 修改样式, 获取缺口图片
        self.driver.execute_script('document.querySelectorAll("canvas")[1].style="opacity: 1; display: none;"')
        # 保存缺口图片
        div_img = self.driver.find_element(By.CLASS_NAME, 'geetest_widget')
        # 截图
        div_img.screenshot(self.gap_img)
        # 执行js代码, 修改元素样式, 获取完整图片
        self.driver.execute_script('document.querySelectorAll("canvas")[2].style=""')
        # 截图
        div_img.screenshot(self.full_img)
        # 修复元素样式
        self.driver.execute_script('document.querySelectorAll("canvas")[1].style="opacity: 1; display: block;"')

    def get_gap(self):
        # 缺口图片
        gap_image = Image.open(self.gap_img)
        # 完整图片
        full_image = Image.open(self.full_img)
        size = gap_image.size
        # 向左偏移量
        left = 0
        for x in range(left, size[0]):
            for y in range(0, size[1]):
                if self.compare_pixels(gap_image, full_image, x, y):
                    left = x
                    return left

    # 对比像素点
    def compare_pixels(self, gap_image, full_image, x, y):
        # 根据坐标加载对应的缺口图像素点
        pixels1 = gap_image.load()[x, y]
        # 根据坐标加载对应的完整背景图像素点
        pixels2 = full_image.load()[x, y]
        print(pixels1, pixels2)
        # 阈值
        threshold = 60
        if abs(pixels1[0] - pixels2[0]) < threshold and abs(pixels1[1] - pixels2[1]) < threshold \
                and abs(pixels1[2] - pixels2[2]) < threshold:
            return False
        return True

    # 滑动函数
    def move_slide(self, offset_x, offset_y, left):
        pyautogui.moveTo(offset_x, offset_y, duration=0.1 + random.uniform(0, 0.1 + random.randint(1, 100) / 100))
        # 按下鼠标，准备开始滑动
        pyautogui.mouseDown()
        offset_y += random.randint(9, 19)
        pyautogui.moveTo(offset_x + int(left * random.randint(15, 25) / 20), offset_y, duration=0.28)
        offset_y += random.randint(-9, 0)
        pyautogui.moveTo(offset_x + int(left * random.randint(17, 23) / 20), offset_y,
                         duration=random.randint(20, 31) / 100)
        offset_y += random.randint(0, 8)
        pyautogui.moveTo(offset_x + int(left * random.randint(19, 21) / 20), offset_y,
                         duration=random.randint(20, 40) / 100)
        offset_y += random.randint(-3, 3)
        pyautogui.moveTo(left + offset_x + random.randint(-3, 3), offset_y,
                         duration=0.5 + random.randint(-10, 10) / 100)
        offset_y += random.randint(-2, 2)
        pyautogui.moveTo(left + offset_x + random.randint(-2, 3), offset_y, duration=0.5 + random.randint(-3, 3) / 100)
        pyautogui.mouseUp()
        time.sleep(3)

    # 鼠标行为链
    def mouse_movements(self, left):
        # 创建鼠标行为链对象
        action = ActionChains(self.driver)
        # 定位滑块
        slider = self.driver.find_element(By.CLASS_NAME, 'geetest_slider_button')
        # 点击, 准备拖拽滑块
        action.click_and_hold(slider)
        # 停顿, 模拟真人
        action.pause(0.5)
        # 移动滑块的距离
        action.move_by_offset(left, 0)
        action.pause(1)
        action.move_by_offset(10, 0)
        action.pause(2)
        action.move_by_offset(-10, 0)
        # 释放鼠标
        action.release()
        # 提交
        action.perform()

    def main(self):
        self.login_img()
        distance = self.get_gap() - 6
        # 方案一: 移动函数
        # self.move_slide(1248, 774, distance)
        # 方案二: 鼠标行为链
        self.mouse_movements(distance)


if __name__ == '__main__':
    sl = Slider()
    sl.main()
