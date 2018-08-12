# from selenium import webdriver
# driver = webdriver.PhantomJS()
# # driver = webdriver.Chrome()
# driver.get('http://www.taobao.com')
# data = driver.page_source
#
# import re
# pattern = '<a .*? href="(.*?)" .*?> | <img src="([^"]+)"[^/]*/>'
#
# for i in re.findall(pattern,data):
#     print (i)
import urllib.request
import urllib.parse
# data = bytes(urllib.parse.urlencode({"word":"name"}),encoding ="utf-8")
# response = urllib.request.urlopen('http://www.httpbin.org/post',data=data)
# print (response.read())
# import urllib.error,socket,time
# try:
#     s = time.time()
#     resp = urllib.request.urlopen('http://www.httpbin.org',timeout=0.1);
# except urllib.error.URLError as e:
#     if isinstance(e.reason,socket.timeout):
#         print('Time Out!')
#         print (time.time()-s)

import requests,re
# from requests.packages import urllib3
#
# url = "http://httpbin.org/"
# response = requests.get(url+"get")
# print (len(response.content ), len(response.text))
# resp = requests.get('https://www.baidu.com')
# print (resp.content.decode('utf8'))
response = requests.get('https://book.douban.com/',headers={"User-Agent":"Mozilla/4.0(compatible;MSIE6.0;WindowsNT5.1"})
data = response.text
# d = '<li class="">.*?<a.*? title="(.*?)">.*?<span>(.*?)</span>.*?<div class="author">(.*?)</div>.*?<p class="abstract">(.*?)</p>.*?</li>'
# pattern = re.compile(d,re.S)
pa = '<li.*?cover">.*?href="(.*?)".*?title="(.*?)".*?author">(.*?)</div>.*?abstract">(.*?)</p>.*?</li>'
pat = re.compile(pa,re.S)
for line in re.findall(pat,data):
    print (line)
