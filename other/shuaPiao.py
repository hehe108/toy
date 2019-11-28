import requests
import threading
import time

#from bs4 import BeautifulSoup

####  151244 yaunxunjie
test_url = 'http://g11364xhfb.haidao13.top/show/vote/vote.ashx?vid=1364&latitude=0&longitude=0&playerid=151244&rand=0.9293619634226229'

def download_page(url):
    headers = {
#'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
'Host': 'g11364xhfb.haidao13.top',
'Accept-Encoding': 'gzip, deflate',
'Cookie': 'openid=oJqfHt7pXp6hW2uCWSALF19037xo_343; ASP.NET_SessionId=ydqmmzyetyhylq55awuo2s45',
'Connection': 'keep-alive',
'Accept': 'application/json, text/javascript, */*; q=0.01',
'User-Agent': 'Mozilla/5.0 (iPod touch; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.4(0x17000428) NetType/WIFI Language/zh_CN',
'Referer': 'http://g11364xhfb.haidao13.top/show/vote/wuhandiamond_9luod8da/9luod8davt.aspx?id=151244&token=s9aqpe&from=timeline&isappinstalled=0',
'Accept-Language': 'zh-cn',
'X-Requested-With': 'XMLHttpRequest'

    }
    data = requests.get(url,headers=headers).content
    return data



def main():
	print("111")
	#print(download_page(test_url).decode('utf-8'))


if __name__ == '__main__':
    main()

	
class MyThread(threading.Thread):
    def __init__(self,arg):
        super(MyThread, self).__init__()#注意：一定要显式的调用父类的初始化函数。
        self.arg=arg
    def run(self):#定义每个线程要运行的函数
        #time.sleep(1)
        #print ('the arg is:%s\r' % self.arg)
        #print ('1111111111111111111')
        #print(download_page(test_url).decode('utf-8'))
        download_page(test_url)

for i in range(4):
    t =MyThread(i)
    t.start()

print ('main thread end')
