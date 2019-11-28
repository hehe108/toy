# _*_ coding:UTF-8 _*
import json
import re
import os


p="/Users/hello/Desktop/rss/"
dirs=os.listdir(p)
dirs.sort()

for dirc in dirs:    
    if dirc.find(".txt")>-1:
        print (p+dirc)
        str=('python3 jjjjjson.py  '+p+dirc)   
        os.system(str)    ##### 生成标题




  
