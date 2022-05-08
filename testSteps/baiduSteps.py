"""
@Time ： 2022/5/8 16:11
@Auth ： heyeping
@File ：baiduSteps.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import os
import time

import allure
from loguru import  logger
from pytest_bdd import given, when, then, parsers, scenario
import pytest
from public.public import get_pathfile
from assertpy import assert_that

feature = os.path.join(get_pathfile(), "features/baidu/baidu.feature")

@allure.feature("测试百度搜索")
@pytest.mark.usefixtures("login_obj")
@scenario(feature, u'访问百度并搜索关键字')
def test_baidu():
    pass

@given(u'访问百度首页')
@allure.step("访问百度首页")
def open_baidu(baidu_obj):
    pass

@when(parsers.parse("输入关键字:{text}"))
@allure.step("输入关键字")
def input_name(baidu_obj, text):
    logger.info(u"开始测试")
    logger.info(u"输入关键字")
    baidu_obj.inputSearch(text)

@when(u'点击搜索按钮')
@allure.step("点击搜索按钮")
def click_btn(baidu_obj):
    baidu_obj.login_button()

@then(parsers.parse("验证返回的搜索结果标题:{result}"))
@allure.step("验证返回的搜索结果")
def assert_result(baidu_obj, result):
    time.sleep(2)
    resultA = baidu_obj.search_result()
    assert_that(resultA).is_equal_to(str(result))
