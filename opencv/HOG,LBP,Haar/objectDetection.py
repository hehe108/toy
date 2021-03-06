# -*- coding: utf-8 -*-

from __future__ import print_function
import cv2 as cv
















if True:
    frame = cv.imread("/Users/hello/Desktop/陈思思 (2) 2.jpg")
    frame = cv.imread("/Users/hello/Desktop/mmexport1546947426207.jpg")
    frame = cv.imread("/Users/hello/Desktop/mmexport1546947420692.jpg")





    face_cascade = cv.CascadeClassifier()
    eyes_cascade = cv.CascadeClassifier()

    #-- 1. Load the cascades
    if not face_cascade.load("./data/haarcascades/haarcascade_frontalface_alt.xml"):
        print('--(!)Error loading face cascade')
        exit(0)
    if not eyes_cascade.load("./data/haarcascades/haarcascade_eye_tree_eyeglasses.xml"):
        print('--(!)Error loading eyes cascade')
        exit(0)



    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_gray = cv.equalizeHist(frame_gray)

    #-- Detect faces
    faces = face_cascade.detectMultiScale(frame_gray)
    for (x,y,w,h) in faces:
        center = (x + w//2, y + h//2)
        frame = cv.ellipse(frame, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 4)

        faceROI = frame_gray[y:y+h,x:x+w]
        #-- In each face, detect eyes
        eyes = eyes_cascade.detectMultiScale(faceROI)
        for (x2,y2,w2,h2) in eyes:
            eye_center = (x + x2 + w2//2, y + y2 + h2//2)
            radius = int(round((w2 + h2)*0.25))
            frame = cv.circle(frame, eye_center, radius, (255, 0, 0 ), 4)

    cv.imshow('Capture - Face detection', frame)    



    ch = cv.waitKey()