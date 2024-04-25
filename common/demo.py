import re
from PIL import Image

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  # 等待类
from urllib import request
from selenium.webdriver.common.action_chains import ActionChains
import random
import time
import cv2


def get_post(img_s):
    # 使用cv2.imread方法读取图片，并将其赋值给变量img
    img = cv2.imread(img_s)
    # 对图片进行高斯滤波，平滑图像，减少噪声
    # blu = cv2.GaussianBlur(img, (5, 5), 0, 0)
    blu = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # print(f'blu:{blu}')
    # 使用Canny边缘检测算法检测图像中的边缘
    canny = cv2.Canny(blu, 50, 150)
    # print(f'canny:{canny}')
    # 查找Canny边缘检测后的图像中的轮廓
    contours, hierarchy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # print(f'contours,hierarchy:{contours,hierarchy}')
    # 打印找到的轮廓数量
    print(f'轮廓数量为{len(contours)}')
    # 遍历所有找到的轮廓
    for i in contours:
        # 获取轮廓的外接矩形，即边界框，包括x, y, w, h坐标和宽度
        x, y, w, h = cv2.boundingRect(i)
        # 计算轮廓的面积
        area = cv2.contourArea(i)
        # 计算轮廓的周长
        zhouzhang = cv2.arcLength(i, True)
        print(f'面积为{area}，周长为{zhouzhang}，x, y, w, h为{x,y,w,h}')

        # 如果轮廓的面积在5025到7225之间，并且周长在300到380之间
        #if 5025 < area < 7225 and 300 < zhouzhang < 380:
        if 10 < area <30 and 15 < zhouzhang <30:
            # 重新获取该轮廓的外接矩形，因为上一个获取的是整个图像的外接矩形，这个才是轮廓的外接矩形
            x, y, w, h = cv2.boundingRect(i)
            # 在原始图像上绘制一个红色的矩形框，标记出满足条件的轮廓位置和大小
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 225), 2)
            # 将绘制了标记的图像保存为'img_122.png'文件
            cv2.imwrite('./img_122.png', img)
            print(f'x:{x}')
            # 返回该轮廓的x坐标值
            return x

            # 如果遍历完所有轮廓后仍未找到满足条件的轮廓，则返回0
    return 0


# 启动浏览器
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://jdapione.fhd001.com/authPlatform.do")

# 定位用户名和密码输入框，并输入相应的用户名和密码
username_input = driver.find_element('id','loginname').send_keys('liujt001')
time.sleep(1)
password_input = driver.find_element('id','nloginpwd').send_keys('Ljt315246')
time.sleep(1)
driver.find_element('id','agree').click()
time.sleep(1)
driver.find_element('id','loginSubmit').click()
time.sleep(10)

#class="JDJRV-bigimg"大图
#class="JDJRV-smallimg"小图
#class="JDJRV-slide-bg "滚动条
# 定位滑块和背景图片元素
# hk = driver.find_element('xpath','//div[@class="JDJRV-slide-inner JDJRV-slide-btn"]')


bg_image = driver.find_element('xpath','//div[@class="JDJRV-bigimg"]')
big_url = bg_image.find_element('tag name','img')
bigurl = big_url.get_attribute('src')

slider=driver.find_element('xpath','//div[@class="JDJRV-smallimg"]')
slider_url = slider.find_element('tag name','img')
sliderurl = slider_url.get_attribute('src')
# print(sliderurl,bigurl)
# 将图片，通过链接保存到本地
request.urlretrieve(bigurl,'./big.jpg')
request.urlretrieve(sliderurl,'./slider.jpg')

dis = get_post('./slider.jpg')
print(dis)
dis = int(dis*340/672 - slider.location['x'])

driver.implicitly_wait(10)
ActionChains(driver).click_and_hold(slider).perform()

# 定义偏移量
i = 0
moved = 0
while moved < dis:
    x = random.randint(3, 10)
    moved += x
    # 滑动距离
    ActionChains(driver).move_by_offset(xoffset=x, yoffset=0).perform()
    print(f"第{i}次移动后，位置为{slider.location['x']}")
    i += 1
ActionChains(driver).release().perform()
time.sleep(10)

driver.get('https://jd.fhd001.com/one/index.html#/myAccount')





time.sleep(3)




