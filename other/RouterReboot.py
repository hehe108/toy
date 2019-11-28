# -*- coding: UTF-8 -*-

import urllib,urllib2
from base64 import encodestring
url='http://192.168.55.1/goform/SysToolReboot'
user='admin'
passwd='admin'
req=urllib2.Request(url)

#req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36')
req.add_header('Authorization',' Basic YWRtaW46YWRtaW4=')
f=urllib2.urlopen(req)
