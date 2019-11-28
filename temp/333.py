# _*_ coding:UTF-8 _*
#if2n
#lf2n
#ivvn

# https://segmentfault.com/q/1010000000124036
import random
import time
import requests
import urllib
import re


aaa= 'hijlfvn2'
count=len(aaa)

#abcdefghijklmnopqrstuvwxyz
#ABCDEFGHIJKLMNOPQRSTUVWXYZ


 



def download_page(url):
	headers = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
	}
	#data = requests.get(url,headers=headers).content
	data = requests.get(url,headers=headers).content

	return data


	
	
	

f = open("text.txt",'a+',encoding='utf-8')




for i in range(0, count):  
   
	
	
	
	
	for j in range(0, count):  


		
		
		
		for h in range(0, count):  


			for k in range(0, count):  
				ddsfsdf=aaa[i]+aaa[j]+aaa[h]+aaa[k]
				
				ddsfsdfdsfdsfds=ddsfsdf.replace('2','')
				
				if len(ddsfsdf)-len(ddsfsdfdsfdsfds)==1:
				
					f.write("www."+ddsfsdf+".com\n")
				

					










				
	
f.close()