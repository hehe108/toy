# _*_ coding:UTF-8 _*
#####  这个只是标题
import json
import re
import sys

'''
def loadFont():
    #f = open("/Users/hello/Desktop/in/1540952083921.txt")  
    f = open(sys.argv[1])  
    setting = json.load(f)
    family = setting['xjxobj'][4]   
    size = family['data']   
    return size

t = loadFont()
'''
#print(t)




f = open(sys.argv[1])
setting = json.load(f)
t = str(setting)



#print (re.search('article_header_title" id="at_\d+">[^/]+</span>', t))
dddd=re.findall('article_header_title" id="at_\d+">([^<]+)</span>', t)
#print (dddd)
#print (re.match('article_header_title" id="at_\d+">[^/]+</span>', t))   ##### 这个是匹配开头
#m=re.search('article_header_title" id="at_\d+">([^/]+)</span>', t)
#print(m.group(1))




f = open("text.txt",'a+',encoding='utf-8')

for i in range(0, len(dddd)):  
    #print i, colour[i] 
    f.write(dddd[i]+"\n")
f.close()