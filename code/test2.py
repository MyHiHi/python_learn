# import pymongo
# client = pymongo.MongoClient('localhost')
# db = client['myUser']
# # db['user01'].insert([{"name":"pyt01","age":12},{"name":"maty","age":22}])
# db['user01'].delete_many({"age":22})
# for i in db['user01'].find({}):
#     print (type(i))
import requests
response = requests.get('https://s1.hdslb.com/bfs/static/jinkela/videoplay/images/anim-collect.png')
with open('../views/images/1.png','wb') as f:
    f.write(response.content)
# print (response.status_code)
# print (response.headers)
# print (response.cookies)
from selenium import webdriver
webdriver.Ph
