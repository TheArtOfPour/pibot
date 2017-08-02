"""Raspberry Pi Face Recognition Treasure Box 
Pi Camera OpenCV Capture Device
Copyright 2013 Tony DiCola 

Pi camera device capture class for OpenCV.  This class allows you to capture a
single image from the pi camera as an OpenCV image.
"""
import io
import time

import cv2
import numpy as np
import picamera

face_cascade = cv2.CascadeClassifier('haar/haarcascade_frontalface_default.xml') 
data = io.BytesIO()
with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    while True:
        camera.capture(data, format='jpeg')
        data2 = np.fromstring(data.getvalue(), dtype=np.uint8)
        image = cv2.imdecode(data2, 1)

        #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        #faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        #for (x,y,w,h) in faces:
        #    cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
        #    roi_gray = gray[y:y+h, x:x+w]
        #    roi_color = image[y:y+h, x:x+w]

        print(data)
        cv2.imshow('image',image)
        k = cv2.waitKey(10)
        if k == 27:         # wait for ESC key to exit and terminate progra,
            cv2.destroyAllWindows()
            break
        #time.sleep(5);
