# 此处就可以导包使用了
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
time.sleep(1)
driver.find_element(By.ID, "kw").send_keys("测试")
time.sleep(1)
driver.find_element(By.ID, "su").click()
time.sleep(1)

driver.quit()
