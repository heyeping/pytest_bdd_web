"""
@Time ： 2022/5/8 14:29
@Auth ： heyeping
@File ：loginSteps.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import os
import allure
from loguru import  logger
from pytest_bdd import given, when, then, parsers, scenario
import pytest
from public.public import get_pathfile

feature = os.path.join(get_pathfile(), "features/loginPage/login.feature")

@allure.feature("登录IMP平台")
@pytest.mark.usefixtures("login_obj")
@scenario(feature, u"用户输入正确的账户和密码进行登录")
def test_login():
    pass

@given(u'打开浏览器且进入登录页面')
def open_loginpage():
    pass

@when(parsers.parse("输入账号:{username}"))
def input_name(login_obj, username):
    logger.info(u"开始测试登录")
    logger.info(u"输入账户")
    login_obj.inputName(username)

@when(parsers.parse("输入密码:{password}"))
def input_password(login_obj, password):
    logger.info(u'输入密码')
    login_obj.inputpsw(password)

@when(u'点击登录按钮')
def click_loginbtn(login_obj):
    login_obj.login_button()


