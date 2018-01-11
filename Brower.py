from selenium import webdriver
import socket
import io
import sys
import time

def simulate_brower(url,n):
    """将浏览器最大化-------------模拟浏览器，谷歌"""

    #模拟谷歌浏览器，启动驱动
    browser = webdriver.Chrome()
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')  # 改变标准输出的默认编码
    browser.get(url)

    #browser.maximize_window() #窗口最大化
    for i in range(n):
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(0.5)
    text = browser.page_source
    browser.close()                 #关闭浏览器
    return str(text)