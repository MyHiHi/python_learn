from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time,re,pymongo
from pyquery import PyQuery as pq

SERVICE_ARGS = ["--load-images=false","--disk-cache=true"]
# browser = webdriver.Chrome()
browser = webdriver.PhantomJS(service_args=SERVICE_ARGS)
browser.set_window_size(1400,900)
wait = WebDriverWait(browser,10)
MONGO_URL = "localhost"
MONGO_DB = "taobao"
MONGO_TABLE = "taobao"

client = pymongo.MongoClient(MONGO_URL,connect=False)[MONGO_DB][MONGO_TABLE]
def search(keyword):
    print ("正在加载....")
    try:
        browser.get("https://www.taobao.com/")
        # q = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"#q")))
        # print (q)
        # click = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#J_TSearchForm > div.search-button > button")))
        # q.send_keys("美食")
        # click.click()
        # total = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > div.total')))
        q = browser.find_element_by_id("q").send_keys(keyword)
        time.sleep(3)
        c = browser.find_element_by_xpath('//*[@id="J_TSearchForm"]/div[1]/button').click()
        time.sleep(3)
        total = browser.find_element_by_css_selector('#mainsrp-pager > div > div > div > div.total').text
        total = int(re.search("(\d+)",total).group(1))
        return total
    except TimeoutException as e:
        return search()

def next_page(page_num):
    print ('正在翻页 ',page_num)
    try:
        q = browser.find_element_by_css_selector('#mainsrp-pager > div > div > div > div.form > input')
        q.clear()
        q.send_keys(page_num)
        time.sleep(3)
        c = browser.find_element_by_xpath('//*[@id="mainsrp-pager"]/div/div/div/div[2]/span[3]').click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"#mainsrp-pager > div > div > div > ul > li.item.active > span",str(page_num))))
        get_products()
    except TimeoutException as e:
        next_page(page_num)

def get_products():
    print ('正在解析 页面')
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"#mainsrp-itemlist .items .item")))
    html = browser.page_source
    doc = pq(html)
    items = doc("#mainsrp-itemlist .items .item").items()
    for item in items:
        product = {
            'image_url':item.find('.pic img').attr('src'),
            'price':item.find('.price').text(),
            'deal':item.find('.deal-cnt').text()[:-3],
            'name':item.find(".title").text().strip(),
            'shop':item.find('.shop').text()
        }
        save_to_mongo(product)

def save_to_mongo(product):
    try:
        if client.insert(product):
            print ('ok')
    except Exception as e:
        print ('error')

def main():
    try:
        total = search(keyword="美食")
        for i in range(1,total+1):
            next_page(i)
    except Exception as e:
        print ("出现异常!")
    finally:
        browser.close()
if __name__ == "__main__":
    main()
