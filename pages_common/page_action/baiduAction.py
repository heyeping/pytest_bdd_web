"""
@Time ： 2022/5/8 16:02
@Auth ： heyeping
@File ：baiduAction.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
from pages_common.page_action.baseAction import BaseAction
from pages_common.page_ui.baiduPage import BaiduPage

class BaiduAction(BaseAction, BaiduPage):

    def inputSearch(self, txt):
        self.clear(self.searchEle)
        self.text_inpit(self.searchEle, txt)

    def login_button(self):
        self.click(self.btnEle)

    def search_result(self):
        return self.driver.title
