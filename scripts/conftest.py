from page_objetc.login_page import Login
from page_objetc.popUp_operation import get_afterLogin,close_ad_popup,close_Newcomer_popup
import pytest
@pytest.fixture(scope='module')
def login_jd():
    '''登陆和关闭首次登陆操作'''
    login_instance = Login()
    driver = login_instance.login_procedure()
    get_afterLogin(driver)
    close_Newcomer_popup(driver)
    close_ad_popup(driver)
    yield driver
    driver.quit()


# @pytest.fixture(scope='session')
# def close(login_jd):
#     driver = login_jd
#     get_afterLogin(driver)
#     close_Newcomer_popup(driver)
#     close_ad_popup(driver)
#     yield driver
