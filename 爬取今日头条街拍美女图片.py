import requests,re,random,json,pymongo,os
from urllib.parse import urlencode
from bs4 import BeautifulSoup
from hashlib import md5
from multiprocessing import Pool

"""
多进程AJAX爬取,下载今日头条的街拍图片并将title和图片URL存入mongodb中
"""

MONGO_URL = "localhost"
MONGO_DB = "toutiao"
MONGO_TABLE = "toutiao"

agents = ["Mozilla/4.0(compatible;MSIE7.0;WindowsNT6.0)",
          "Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
          "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Maxthon2.0)"]

db = pymongo.MongoClient(MONGO_URL,connect=False)[MONGO_DB]

def get_page_text(offset):
    args = {
        "offset": offset,
        "format": "json",
        "keyword": '街拍',
        "autoload": "true",
        "count": 20,
        "cur_tab": 1,
        "from": "search_tab"
    }
    url = "https://www.toutiao.com/search_content/?"+urlencode(args)
    try:
        resp= requests.get(url,headers={"User-Agent":random.choice(agents)})
        if resp.status_code==200:
            return resp.text
        return  None
    except Exception as e:
        print ("GET失败")
        return None

def parse_page_text(text):
    text = json.loads(text)
    try:
        if text and "data" in text.keys():
            for data in text.get("data"):
                yield data.get("article_url")
        else:
            return None
    except:
        return None

def get_page_detail(url):
    try:
        resp= requests.get(url,headers={"User-Agent":random.choice(agents)})
        if resp.status_code==200:
            return resp.text
        return  None
    except Exception as e:
        print ("GET失败")
        return None

def parse_page_detail(html):
    if not html:
        return None
    bs = BeautifulSoup(html,"lxml")
    title = bs.title.string
    pa = re.search("var gallery = (.*?);",html,re.S)
    if not pa:
        return None
    images=[]
    pa = json.loads(pa.group(1))
    if "sub_images" in pa.keys():
        for url in pa.get("sub_images"):
            images.append(url.get("url"))
        return {
            "title":title,
            "images":images
        }
    return None

def save_to_mongo(result):
    if db[MONGO_TABLE].insert(result):
        print ("ok")
        return True;
    else:
        return False

def download_images(url):
    print ("download: "+url)
    try:
        resp= requests.get(url,headers={"User-Agent":random.choice(agents)})
        if resp.status_code==200:
            save_images(resp.content)
        return  None
    except Exception as e:
        print(e)
        print ("GET图片失败")
        return None
def save_images(content):
    file_path = r"{0}/images/{1}.{2}".format(os.getcwd(),md5(content).hexdigest(),"jpg")
    if not os.path.exists(file_path):
        with open(file_path,"wb") as f:
            f.write(content)
def main(offset):
    text = get_page_text(offset=offset)
    for article_url in parse_page_text(text):
        html = get_page_detail(article_url)
        result = parse_page_detail(html)
        if not result:
            continue
        save_to_mongo(result)
        for url in result.get("images"):
            download_images(url="http:"+url)

if __name__ == "__main__":
    pool = Pool()
    pool.map(main,[x*20 for x in range(0,6)])

