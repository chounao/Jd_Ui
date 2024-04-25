from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def openurl(self, url):
        """定义打开url方法"""
        try:
            self.driver.get(url)
            self.driver.maximize_window()
            self.driver.implicitly_wait(3)
        except Exception as e:
            raise ValueError(e)
        return self.driver



    def find_element(self, selectors):
        element_by = selectors[0]
        element_value = selectors[1]

        """
        @param selectors:
        @return: 返回查找元素的结果
        """

        try:
            if element_by in ['id', 'name', 'class', 'tag', 'link', 'plink', 'css', 'xpath']:
                by_map = {
                    'id': By.ID,
                    'name': By.NAME,
                    'class': By.CLASS_NAME,
                    'tag': By.TAG_NAME,
                    'link': By.LINK_TEXT,
                    'plink': By.PARTIAL_LINK_TEXT,
                    'css': By.CSS_SELECTOR,
                    'xpath': By.XPATH
                }
                by = by_map[element_by]
                return WebDriverWait(self.driver, 10, 0.5).until(
                    EC.visibility_of(self.driver.find_element(by, element_value)))
            else:
                raise NameError("请输入可查找的元素.")
        except Exception as e:
            raise e


    def insert_value(self, selectors,value):
        """
        @param selectors:
        @param value: 输入send_keys值进行输入操作
        @return: 页面输入值
        """
        element = self.find_element(selectors)
        element.send_keys(value)
    def touch_click(self,selectors):
        """
        @param selectors:
        @return: 点击按钮
        """
        elemnt = self.find_element(selectors)
        elemnt.click()

    def get_url(self):
        current_url = self.driver.current_url
        return current_url
