# p={"小华":90,"小op":88}
# for i in p:
#     print(i)
#
# dict = {"k1":"v1","k2":"v2"}
# print("this is %(k1)s and %(k2)s"%dict)

# from selenium import  webdriver
# import time
# agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
# driver = webdriver.Chrome()
# driver.get('https://mail.qq.com/')
# time.sleep(15)
# driver.find_element_by_xpath('//*[@id="u"]').clear()
# driver.find_element_by_xpath('//*[@id="u"]').send_keys('909535692')
# time.sleep(5)
# driver.find_element_by_xpath('//*[@id="p"]').clear()
# driver.find_element_by_xpath('//*[@id="p"]').send_keys('747474111')
#
# time.sleep(5)
# driver.find_element_by_xpath('//*[@id="p_low_login_enable"]').click()
#
# time.sleep(5)
# driver.find_element_by_xpath('//*[@id="login_button"]').click()
#
# print(driver.get_cookies())
import lxml
from selenium import webdriver

cc = webdriver.PhantomJS()
cc.get("http://www.baidu.com")
from bs4 import BeautifulSoup
aa = BeautifulSoup(cc.page_source,'lxml')
print(aa.text)
# import selenium.webdriver.support.ui as ui
#
# driver_item=webdriver.Chrome()
# url="https://movie.douban.com/"
# wait = ui.WebDriverWait(driver_item,10)
# driver_item.get(url)
# wait.until(lambda driver: driver.find_element_by_xpath("//div[@class='fliter-wp']/div/form/div/div/label[5]"))
# driver_item.find_element_by_xpath("//div[@class='fliter-wp']/div/form/div/div/label[5]").click()
