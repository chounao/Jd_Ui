from data.popUps_data import PopupNotification
from common.BeasPage import BasePage
import time

def get_afterLogin(driver):
    '''
    判断登陆后是否为首页，如果不是重制url
    :param driver:
    :return:
    '''
    driver = BasePage(driver)
    time.sleep(5)
    current_url = driver.get_url()
    url = 'https://jd.fhd001.com/one/index.html#/tradesAuto'
    if url != current_url:
        try:
            driver.openurl(url)
        except ValueError as e:
            raise e
    else:
        print('URL正常')

def close_popup(driver,popup,closeBtn):
    '''
    封装关闭弹窗操作
    :param driver:
    :param popup_selectors:
    :param closeBtn_selectors:
    :param expected_text:
    :return:
    '''
    driver = BasePage(driver)
    time.sleep(10)
    try:
        driver.find_element(popup)
        try:
            driver.touch_click(closeBtn)
        except ValueError as e:
            raise e
    except ValueError as e:
        raise e

def close_Newcomer_popup(driver):
    close_popup(driver, PopupNotification.Newcomer_popup_selectors, PopupNotification.Newcomer_closeBtn_selectors)

def close_ad_popup(driver):
    close_popup(driver, PopupNotification.ad_selectors, PopupNotification.ad_closeBtn_selectors)


