# -*- coding: utf-8 -*-

from __future__ import print_function
import cv2 as cv
















if True:
    frame = cv.imread("/Users/hello/Desktop/陈思思 (2) 2.jpg")
    frame = cv.imread("/Users/hello/Desktop/mmexport1546947426207.jpg")
    frame = cv.imread("/Users/hello/Desktop/mmexport1546947420692.jpg")





    face_cascade = cv.CascadeClassifier()


    #-- 1. Load the cascades
    xml="./data/haarcascades/haarcascade_frontalface_alt.xml"
    xml="./data/hogcascades/hogcascade_pedestrians.xml"  ###HOG cascade is not supported in 3.0 in function 'read
    xml="./data/lbpcascades/lbpcascade_frontalface.xml"  
    xml="./data/haarcascades/haarcascade_smile.xml"
    
    if not face_cascade.load(xml):
        print('--(!)Error loading face cascade')
        exit(0)




    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_gray = cv.equalizeHist(frame_gray)

    #-- Detect faces
    faces = face_cascade.detectMultiScale(frame_gray)
    for (x,y,w,h) in faces:
        center = (x + w//2, y + h//2)
        frame = cv.ellipse(frame, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 4)


    cv.imshow('Capture - Face detection', frame)    



    ch = cv.waitKey()