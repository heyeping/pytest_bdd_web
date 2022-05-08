"""
@Time ： 2022/5/8 14:31
@Auth ： heyeping
@File ：conftest.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

import pytest
from pages_common.page_action.loginAction import LoginAction


@pytest.fixture(scope="module")
def login_obj():
    loginaction = LoginAction()
    yield loginaction