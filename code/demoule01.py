# coding:utf-8

from selenium import webdriver

import time
import json

driver = webdriver.Chrome()
# driver.get('https://wx.qq.com/')

driver.get('https://mail.qq.com/')

driver.find_element_by_xpath('//*[@id="u"]').clear()
driver.find_element_by_xpath('//*[@id="u"]').send_keys('909535692')
time.sleep(2)
driver.find_element_by_xpath('//*[@id="p"]').clear()
driver.find_element_by_xpath('//*[@id="p"]').send_keys('747474111')
time.sleep(2)
driver.find_element_by_xpath('//*[@id="p_low_login_enable"]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="dologin"]').click()

time.sleep(12)
cookie = driver.get_cookies()

cookies = {}
for item in cookie:
    cookies[item.get('name')] = item.get('value')

try:
    file = open('cookies.txt', 'wb')
except Exception as e:
    print(e)
else:
    file.write(json.dumps(cookies))
    file.close()
finally:
    driver.close()
