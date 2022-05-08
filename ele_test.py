"""
@Time ： 2022/5/8 15:38
@Auth ： heyeping
@File ：ele_test.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
#封装元素方法
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
import time
class Base():
    def __init__(self,driver):
        self.driver=driver

    #查找元素
    def find_element(self,locator):#locator参数是定位方式，如("id", "kw"),把两个参数合并为一个,*号是把两个参数分开传值
        element=WebDriverWait(self.driver,20,0.5).until(lambda x:x.find_element(*locator))
        return element
    #判断元素是否存在
    def is_exists(self,locator):
        try:
            WebDriverWait(self.driver,20,0.5).until(lambda x:x.find_element(*locator))
            return True
        except:
            return False
    #判断元素是否已经不存在,不存在了返回True,还存在就返回False
    def element_is_disappeared(self,locator,timeout=30):
        is_disappeared=WebDriverWait(self.driver,timeout,1,(ElementNotVisibleException)).until_not(lambda x:x.find_element(*locator).is_displayed())
        print(is_disappeared)

    #封装一个send_keys
    def send_keys(self,locator,text):
        self.find_element(locator).send_keys(text)

    #封装一个click
    def click(self,locator):
        self.find_element(locator).click()

#运行主函数
if __name__=='__main__':
    driver=webdriver.Chrome()
    driver.get("https://imp.leedarson.com/login?mode=account")
    #实例化
    base=Base(driver)
    #定位输入框
    input_loc=("xpath",'//*[@id="root"]/section/main/div[2]/form/div[1]/div/div')
    #通过实例调用find_element来发送
    base.send_keys(input_loc,"selenium")
    #点击按钮
    #button_loc=("id","su")
    #base.click(button_loc)

    time.sleep(3)
    driver.quit()
