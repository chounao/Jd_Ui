import pytest
# from page_objetc.myAccount_page import Account
from page_objetc.myAccount_page import click_btn

# def test_account(login_jd):
#     a= Account()
#     a.click_btn(login_jd)
''

def test_account(login_jd):
    click_btn(login_jd)


if __name__ == '__main__':
    pytest.main(['-vs',r'./test_001.py'])