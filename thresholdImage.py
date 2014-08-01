###########################################
## thresholdingImage.py
## 
## Converts an image file to binary, then writes pixel values to CSV
##
## Author: Kevin T. Lee
###########################################

import sys, cv2, csv, os
import numpy as np
from PIL import Image


# Set imageName variable
imageName = 'square1.jpg'

# Read iamgeName file
sourceImage = cv2.imread(imageName, 0)

## color to gray scale
#grayImage = cv2.cvtColor(sourceImage, cv2.COLOR_RGB2GRAY) # cv2.COLOR_RGB2GRAY = 7
#grayImgName = 'gray_' + imageName
 
 ## gray to binary: threshold = 100 (arbitrary); maxValue = 255; type = cv2.THRESH_BINARY
flag, binaryImage = cv2.threshold(sourceImage, 65, 255, cv2.THRESH_BINARY) # cv2.THRESH_BINARY = 0
binaryImgName = 'binary_' + imageName

#cv2.imshow('main', binaryImage)
cv2.imwrite(binaryImgName, binaryImage)


#Get pixels in image, store pixel values
im = Image.open(binaryImgName)
pixels = list(im.getdata())

# Debug print statement - pixel array
#print(pixels)


#Write CSV file with shape data (pixel values)
fl = open('shapedataIMAG19.csv', 'w')

writer = csv.writer(fl, lineterminator='\n')

labelRow = ['label']
for i, val in enumerate(pixels):
    labelRow.append('pixel'+str(i))


writer.writerow(labelRow)
writer.writerow(pixels)

fl.close() 

