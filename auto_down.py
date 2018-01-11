import socket
from urllib import request
import os

def auto_down(imgList):
    #删除创建文件夹
    try:
        os.mkdir('./Img')
        print("文件夹已创建。")
    except:
        print("文件夹已存在。")
    print("即将开始下载：")
    x = 0  # 文件名，递增
    print(x)

    # 设置全局超时函数
    socket.setdefaulttimeout(1)

    for imgA in imgList:
        try:
            if (len(imgA) <= 200):
                request.urlretrieve(imgA, './Img/%s.jpg' % x)
                print("%s---" % x, imgA, end=" \n下载成功\n")
                x += 1
        except:
            print("-----", imgA, end=" \n下载失败\n")
            pass
    print("下载链接总数： ", len(imgList))
    print("下载成功总数： ", x - 1)
    print("下载失败总数： ", (len(imgList) - x + 1))