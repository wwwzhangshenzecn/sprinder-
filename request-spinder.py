import re
import time
import inFfile
import Brower
import auto_down

def getHtml(url,n):
    html = Brower.simulate_brower(url,n)
    inFfile.in_file(html)
    return html

def getData(Html,n=3):
    html =getHtml(Html,n)        #获取html内容

    #data-objurl="http://old.bz55.com/uploads/allimg/140321/1-140321114352.jpg" data-thumburl
    reg = r'data-objurl="(http:.+?\.jpg)" data-thumburl'            #正则表达式
    imgReg =re.compile(reg)

    t2=time.time()
    imgList = re.findall(imgReg,html)    #匹配正则
    t3 = time.time()

    print("计算需下载链接总数：",len(imgList))
    print("耗时：",(t3-t2))
    #print(imgList)

    t4 = time.time()
    auto_down.auto_down(imgList)
    t5 = time.time()
    print("下载耗时：%d s" % (t5 - t4))


url=str(input("输入网页："))
n = int(input("输入页面滚动次数：") )
print("正在下载，请等候......")
getData(url,n)
print("按任意键退出。")
input()
