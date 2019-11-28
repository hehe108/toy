import urlparse
import sys
import os
u='http://www.baidu.com/112312/234234/index.php?aaaa=bbb'


u=sys.argv[1]
url=urlparse.urlparse(u)
print url



pppp=  url.path.split("/")

l=len(pppp)






#print os.getcwd()

fileName=pppp[l-1]
savePath =os.getcwd()+"/down/"+url.netloc+"/"+url.path.replace(pppp[l-1],'').replace(pppp[0],'')



os.system("mkdir  -p "+savePath)





os.system(" wget "+u+"  -O   "+savePath+""+fileName)
