import os
import time

def in_file(html):
    try:
        os.remove('html.txt')
        print("删除文件...")
    except:
        pass
    # print(html)
    print("正在写入文件，请稍等......")

    try:
        # 打开文件
        fmk = os.open("html.txt", os.O_RDWR | os.O_CREAT)
        # 获取以上文件的对象
        f = os.fdopen(fmk, "wb+")  # -----------wb+模式

        t0 = time.time()

        f.write(html.encode('utf-8'))  # ------------写入文件

        t1 = time.time()

        print('写入文件html.txt------耗时：', (t1 - t0))
    except:
        print("写入失败，退出！")
        exit()