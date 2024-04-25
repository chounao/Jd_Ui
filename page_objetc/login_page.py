from common.BeasPage import BasePage
from common.driver import WDriver
from data.login_data import LoginPageData
from data.read_ini import get_ini_data
import time

class Login(BasePage):

    def __init__(self):
        self.base_page = BasePage(WDriver().chromeDriver())

    def login_page(self, args):
        '''
        打开登录页面
        :param args:
        :return:
        '''

        value = get_ini_data(args)
        self.base_page.openurl(str(value))

    def input_data(self, selector, args):
        '''
        查找输入框并输入数据
        :param selector:
        :param args:
        :return:
        '''
        value = get_ini_data(args)
        # print(value)
        try:
            self.base_page.insert_value(selector, value)
        except Exception as e:
            raise ValueError(e)

    def click_data(self, selector):
        '''
        勾选同意/点击登录按钮
        :param selector:
        :return:
        '''
        try:
            self.base_page.touch_click(selector)
        except Exception as e:
            raise ValueError(e)
        return self.base_page.driver

    def login_procedure(self):
        self.login_page(['HTTP', 'login_url'])
        self.input_data(LoginPageData.username_selectors, ['LOGIN', 'UserName'])

        self.input_data(LoginPageData.password_selectors, ['LOGIN', 'PassWorld'])

        self.click_data(LoginPageData.agreeBtn_selectors)
        print("点了勾选")
        self.click_data(LoginPageData.loginBtn_selectors)
        print('点了登陆')
        self.driver = self.base_page.driver
        print('登陆')
        time.sleep(10000)
        return self.driver


if __name__ == '__main__':
    a = Login()
    a.login_procedure()
