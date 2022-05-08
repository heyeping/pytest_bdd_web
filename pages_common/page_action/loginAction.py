"""
@Time ： 2022/5/8 14:21
@Auth ： heyeping
@File ：loginAction.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

import logging
from pages_common.page_action.baseAction import BaseAction
from pages_common.page_ui.loginPage import LoginPage

class LoginAction(BaseAction, LoginPage):

    def inputName(self, username):
        self.clear(self.usernameEle)
        self.text_inpit(self.usernameEle, username)

    def inputpsw(self, password):
        self.clear(self.passwordEle)
        self.text_inpit(self.passwordEle, password)

    def login_button(self):
        self.click(self.login_btu())
