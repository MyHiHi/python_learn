# coding:utf-8
import json
import requests

header={
    "Host": "music.163.com",
    "Referer": "https://mail.163.com/js6/main.jsp?sid=fBheAQNNCeElNgOSuGNNyRFZYqCPKFFX&df=mail163_letter",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
}
cookie = "starttime=; mail_login_way=normal; NTES_SESS=ZTQghZo7EpehxzFTkGnHUaNGKeX8bJr9smFtJFaUb.AXCIEACNjlM8EfkSKm0BvMVVo93u1TKWCu8cfas1YwNo2zombEe93_5RLggZssI9AC_g3biQ.t8F7rBe0lgeZNMtC9TWh7ge5jpn_gQy9jutfw5KHDaNxAA_elEsXkxNJ_D_gw5EC69pbtVI9inC4ZJ; NTES_PASSPORT=Dj82f4PWwakaJbZn7KDQHcSdIJUMZGMebsU0Oe6AhvfG7LHE7Muc9bHNAImdWRQ93ApGX6vmdPwlsvnpmbbnbk7w7bqJFXKD9.P02GF8GA2HFkRiMCBUHKXpiSt3ZsJ1yUODntufzA95v2IoOaKVN9lKZAN.K3oSoo4Cs9qoPegMcNqjeY9YgvEvc; S_INFO=1528080024|0|3&80##|ztaosome; P_INFO=ztaosome@163.com|1528080024|1|mail163|00&99|heb&1524465167&other#heb&130100#10#0#0|&0||ztaosome@163.com; nts_mail_user=ztaosome@163.com:-1:1; df=mail163_letter; mail_psc_fingerprint=042351a832939635b4cedd22c9266ede"
cookies={}
for line in cookie.split(';'):
    data = line.split('=')
    cookies[data[0]]=data[1]
requests.get(url="https://mail.163.com/",cookies= cookies)


data={
    "sid": "fBheAQNNCeElNgOSuGNNyRFZYqCPKFFX",
    "df": "mail163_letter"
}
url = "https://mail.163.com/js6/main.jsp?sid=fBheAQNNCeElNgOSuGNNyRFZYqCPKFFX&df=mail163_letter"
# requests.get(url, cookies=cookies,headers=header)
response = requests.post(url, cookies=cookies, headers=header, data=data)
content = response.json().get('list')
for items in content:
    title = items.get('title')
    url = items.get('url')
    print(title, url)
