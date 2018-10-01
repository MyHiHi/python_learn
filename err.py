#coding=gbk
import requests,os,subprocess,time
from multiprocessing.dummy import Pool as ThreadPool
from pyquery import PyQuery as pyq

count = 0
foldName = str(time.strftime("%Y-%m-%d"))
def getInfo(url):
    text = requests.get(url).text
    return text

def getSrc(url):
    text = getInfo(url)
    doc = pyq(text)
    cts = doc('.thumb_mov_model').find('a')
    for i in cts:
        link = pyq(i).attr('href')
        src = pyq(getInfo(link))('#example_video_1').find('source').attr('src')
        yield src

def download(url):

    for src in getSrc(url):
        if src:
            print(src)
            file_name = str(src).split('/')[-1]
            print(file_name+" STARTS")
            global count
            count+=1
            os.system(r'you-get -o L:\myFile\didis\{0} -O {1} {2}'.format(foldName ,count, src))
if __name__ == "__main__":
    pool = ThreadPool(8);
    url_list = []
    while 1:
        try:
            i,j = int(input("输入起始值")),int(input("输入终止值"))
            if (str(input("是否删除原文件(y/n)")) == "y"):
                os.system(r'del L:\myFile\didis\{0} /q'.format(foldName))
            if i<j:
                for i in range(i,j):
                        url_list.append('https://www.sexhound.xxx/categories/muscle/'+str(i)+'/')
                        pool.map(download,url_list)
                        pool.close()
                        pool.join()

                break;
            else:
                print('输入正确值')
        except Exception as e:
            print('输入整数哦！')

    print('运行完毕! 总共{0}条'.format(count))

