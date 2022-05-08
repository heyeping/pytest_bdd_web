"""
@Time ： 2022/5/5 21:06
@Auth ： heyeping
@File ：driverCreate.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

import pytest
from selenium import webdriver
from public.public import Signal

class DriverCreate(Signal):
    def get_driver(self):
        if not hasattr(self, '_driver'):
            self._driver = webdriver.Chrome()
            self._driver.maximize_window()
            self._driver.get("https://imp.leedarson.com/login?mode=account")
            self.driver = self._driver
        return self.driver