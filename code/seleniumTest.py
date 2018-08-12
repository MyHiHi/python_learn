from selenium import webdriver
# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')
# lis = browser.find_element_by_css_selector(".service-bd li")
# print (lis)
from pyquery  import PyQuery
query = PyQuery(url="https://www.taobao.com/")
q = query(".J_Cat.a-all a").items()
for i in q:
    print(i.text())
