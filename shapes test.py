###########################################
## shapes test.py
###########################################

import numpy as np
import cv2
import csv
import sys, os
from PIL import Image

#set size for resize
size = 200, 200

#resize image
try:
    im = Image.open('IMAG19result.png')
    #im = im.convert('L') #convert to grayscale
    #im = im.convert('1') #convert to monochrome
    im.thumbnail(size, Image.ANTIALIAS)
    im.save('IMAG19result.png')
except IOError:
    print "cannot create thumbnail for '%s'" % infile

#Get pixels in image
pixels = list(im.getdata())

# Determine shape by contour, prepend to pixel list for CSV
img = cv2.imread('IMAG19result.png')
gray = cv2.imread('IMAG19result.png',0)

ret,thresh = cv2.threshold(gray,127,255,1)

contours,h = cv2.findContours(thresh,1,2)

for cnt in contours:
     approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
     print len(approx)
     if len(approx)==5:
         print "pentagon"
         pixels.insert(0, "pentagon")
         #cv2.drawContours(img,[cnt],0,255,-1)
     elif len(approx)==3:
         print "triangle"
         pixels.insert(0, "triangle")
         #cv2.drawContours(img,[cnt],0,(0,255,0),-1)
     elif len(approx)==4:
         print "square"
         pixels.insert(0, "square")
         #cv2.drawContours(img,[cnt],0,(0,0,255),-1)
     elif len(approx) == 9:
         print "half-circle"
         pixels.insert(0, "half-circle")
         #cv2.drawContours(img,[cnt],0,(255,255,0),-1)
     elif len(approx) > 15:
         print "circle"
         pixels.insert(0, "circle")
         #cv2.drawContours(img,[cnt],0,(0,255,255),-1)


# Debug print statement - pixel array
print(pixels)


#Write CSV file with shape data
fl = open('shapedataIMAG19.csv', 'w')

writer = csv.writer(fl, lineterminator='\n')

labelRow = ['label']
for i, val in enumerate(pixels):
    labelRow.append('pixel'+str(i))


writer.writerow(labelRow)
writer.writerow(pixels)

fl.close() 




#cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
