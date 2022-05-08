"""
@Time ： 2022/5/8 14:06
@Auth ： heyeping
@File ：baseAction.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
from public.driverCreate import DriverCreate
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class BaseAction(object):

    def __init__(self,):
        self.driver = DriverCreate().get_driver()
        self.wait = WebDriverWait(self.driver, 10)

    def find_Ele(self, ele):
        return self.wait.until(EC.presence_of_element_located(ele))

    def click(self, ele):
        element = self.find_Ele(ele)
        element.click()

    def text_inpit(self,ele, value):
        element = self.find_Ele(ele)
        time.sleep(2)
        element.send_keys(value)

    def clear(self, ele):
        element = self.find_Ele(ele)
        element.clear()