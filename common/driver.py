from selenium import webdriver
import platform

class WDriver(object):
    def chromeDriver(self):
        '''
        这里判断了当前的系统如果是windows，根据系统调用驱动
        :param path_name: 驱动的路径，可以把驱动放在代码文件里面写死路径
        :return:
        '''

        chrome_options = webdriver.ChromeOptions()
        self.system = platform.system()
        try:
            if self.system == "Windows":
                # path_name = 'C:/Users/86185/AppData/Local/Programs/Python/Python39/chromedriver.exe'
                # self.driver = webdriver.Chrome(executable_path=path_name, chrome_options=chrome_options)
                 chrome_options.binary_location = r'C:\Users\86185\AppData\Local\Programs\Python\Python39\chromedriver.exe'
                 self.driver = webdriver.Chrome()
            elif self.system == "Darwin":
                self.driver = webdriver.Chrome()
        except Exception as e:
            raise ValueError(e)
        return self.driver
    def firefoxDriver(self):
        try:
            self.driver = webdriver.Firefox()
        except Exception as e:
            raise ValueError (e)
        else:
            return self.driver

