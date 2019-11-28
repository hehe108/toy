# -*- coding: utf-8 -*-
import os






ffff = open("text.txt",'a+',encoding='utf-8')



for fpathe,dirs,fs in os.walk('/Users/hello/Desktop/opencv/opencv-master/samples/python'):
    for f in fs:
        #print (os.path.join(fpathe,f))
        #ffff.write(os.path.join(fpathe,f)+"\n")
        ffff.write(os.path.join(fpathe,f)+"\n")



    
ffff.close()