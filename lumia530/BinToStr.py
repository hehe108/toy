# -*- coding: utf-8 -*-
# 先凑活用吧  以后计数的 

import sys




def abc( num,len ):
	if  num==len or num<0:
		return  True
	else : 
		return	(buf[num]<123 and buf[num]>96 )  or (buf[num]<91 and buf[num]>64)











#stream = open('新建文本文档.txt', 'rb')


stream = open(sys.argv[1], 'rb')

buf = stream.read()


print(buf[14])


print(chr(buf[14]))


print(  " A 的ASCII 码为", ord('A'))
print(  " Z 的ASCII 码为", ord('Z'))

print(  " a 的ASCII 码为", ord('a'))
print(  " z 的ASCII 码为", ord('z'))


ppppp=" "
for num in range(0,len(buf)):
	isABCZXY=abc(num,len(buf))
	
	isABCZXY2=abc(num-1,len(buf))
	
	isABCZXY3=abc(num+1,len(buf))
	if isABCZXY     and (isABCZXY2 or isABCZXY3 )    : #  前一个 跟 下一个 不是 是空格 
		print(chr(buf[num]), end='')
		ppppp=""
	else:
		if ppppp=="" :
			print("", end=' ')
			ppppp=" "
			





	