# -*- coding: utf-8 -*-
import cv2

cam = cv2.VideoCapture(0)
s, im = cam.read() # captures image
cv2.imshow('Test Picture', im) # displays captured image
cv2.imwrite("test.bmp",im) 


if cv2.waitKey(0) & 0xFF == ord('q'):
    cam.release()


cv2.destroyAllWindows()
