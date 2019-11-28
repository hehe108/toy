# -*- coding: utf-8 -*-
import os

def gci(filepath):

  ffff = open("text.txt",'a+',encoding='utf-8')

  files = os.listdir(filepath)
  files.sort()
  for fi in files:
    fi_d = os.path.join(filepath,fi)            
    if os.path.isdir(fi_d):
      gci(fi_d)                  
    else:
      print(os.path.join(filepath,fi_d) )
      if os.path.join(filepath,fi_d).find(".py")>-1:
         ffff.write(os.path.join(filepath,fi_d)+"\n")
  ffff.close()

gci('/Users/hello/Desktop/opencv/opencv-master/samples/python')





        



    
