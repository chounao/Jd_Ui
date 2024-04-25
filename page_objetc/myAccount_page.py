from common.BeasPage import BasePage
from data.myAccount_data import AccountPlatform
import time
# class Account(BasePage):
#     def __init__(self,driver):
#         self.driver =driver
#
#     def click_btn(self,dir):
#
#         self.driver = BasePage(dir)
#         try:
#             # BasePage(self.driver).openurl('https://jd.fhd001.com/one/index.html#/myAccount')
#             self.driver.openurl('https://jd.fhd001.com/one/index.html#/myAccount')
#         except ValueError as e:
#             raise (e)
#         try:
#             self.driver.touch_click(AccountPlatform.associatedRecords_selectors)
#         except ValueError as e:
#             raise (e)
#         return self.driver

def click_btn(driver):

    driver = BasePage(driver)
    try:
        time.sleep(10)
        # BasePage(self.driver).openurl('https://jd.fhd001.com/one/index.html#/myAccount')
        driver.openurl('https://jd.fhd001.com/one/index.html#/myAccount')
    except ValueError as e:
        raise (e)
    try:
        driver.touch_click(AccountPlatform.associatedRecords_selectors)
    except ValueError as e:
        raise (e)
    return driver



