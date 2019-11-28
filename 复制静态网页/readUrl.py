import urlparse
import sys
import os





for line in open("url.txt"): 
    print line


    str=('python down.py  '+line)   
    os.system(str)