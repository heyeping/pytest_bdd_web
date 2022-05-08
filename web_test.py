"""
@Time ： 2022/5/8 15:31
@Auth ： heyeping
@File ：web_test.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://imp.leedarson.com/login?mode=account")
time.sleep(2)
ele = WebDriverWait(driver, 15, 0.5).until(EC.visibility_of_element_located(("id", 'phoneNumber')))
ele.send_keys("测试")
time.sleep(2)
driver.close()