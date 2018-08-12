import requests
import re
url = "https://movie.douban.com/chart"
response = requests.get(url).content.decode('utf-8')
pattern = '<div class="pl2">.*?>(.*?)<span style="font-size:13px;">'

k=0;
for i in re.findall(pattern, response,re.S):
    if (k%2==0):
        for kiki in i.split(' '):
            if (kiki=='' or kiki=='\n' or kiki=='/'):
                pass;
            else:
                with open('movieList.txt',"a") as f:
                    f.write(kiki+"\r\n")
                    print(kiki)
    else:
        pass
    k+=1;


#
#
# import urllib.request
# import re  #正则表达式
# import datetime  #计时
#
# starttime = datetime.datetime.now()
# for i in (0,25,75,100,125,175,200,225):  #循环网页
#     urll='https://movie.douban.com/top250?start='+str(i)+'&filter='
#     response = urllib.request.urlopen(urll)
#     html = response.read().decode('utf-8')  # 获取网页代码
#     print(html)
#     # result = re.findall('<em class="">(.*?)</em>.*?alt=(.*?)src=', html, re.S)
#     # for j in result:
#     #     print(j)
#     #     print(j[1])
# endtime = datetime.datetime.now()
# time = (endtime - starttime).seconds
# print('总共用时：%s s' % time)  #打印用时
