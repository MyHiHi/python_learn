
# coding:utf-8
import os

def showFiles(path):
    paths=[]
    paths.append(path)
    while len(paths):
        dirPath = paths.pop()
        for file in os.listdir(dirPath):
            fileDir = os.path.join(dirPath,file)
            if os.path.isfile(fileDir):
                dirList = fileDir.split('.')
                if dirList[-1]=='html':
                    with open(r'e:\exe.txt', 'a') as f:
                        f.write(fileDir + "\n")
            else:
                paths.append(fileDir)


if __name__=="__main__":
    # path = str(input("输入地址"))
    # path = r'F:\new'
    # showFiles(path)
    with open(r'e:\exe.txt', 'r') as f:
        print len(f.readlines())

