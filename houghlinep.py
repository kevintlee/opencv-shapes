###########################################
## houghlinep.py
## 
## Find hough lines, OPENCV2 Code
##
## Author: Kevin T. Lee
## Credits: OpenCV2
###########################################

import cv2
import numpy as np

img = cv2.imread('twobox.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)

minLineLength = 100
maxLineGap = 10

lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
for x1,y1,x2,y2 in lines[0]:
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),5)

cv2.imwrite('twobox houghlinep.jpg',img)
