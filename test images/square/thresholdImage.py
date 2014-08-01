###########################################
## thresholdingImage.py
## 
## Converts an image file to binary, then writes pixel values to CSV
##
## Author: Kevin T. Lee
###########################################

import sys, os, cv2, csv
import numpy as np
from PIL import Image

# Create array of shapes 
shapes = ['square', 'circle', 'triangle']
imagePixelList = []

# Loop through array of shapes to get images from file and get iamge data
for i,val in enumerate(shapes):
    for root, dirs, files in os.walk("C:/Users/ktl29155/Desktop/opencv-shapes/test images/" + shapes[i]):
        labelRow = ['label']
        pixelRow = [shapes[i]]

        for fileName in files:
            imageName = fileName

            try:
                sourceImage = cv2.imread(fileName, 0)

                ## color to gray scale
                #grayImage = cv2.cvtColor(sourceImage, cv2.COLOR_RGB2GRAY) # cv2.COLOR_RGB2GRAY = 7
                #grayImgName = 'gray_' + imageName
                 
                 ## gray to binary: threshold = 100 (arbitrary); maxValue = 255; type = cv2.THRESH_BINARY
                flag, binaryImage = cv2.threshold(sourceImage, 65, 255, cv2.THRESH_BINARY) # cv2.THRESH_BINARY = 0
                binaryImgName = 'binary_' + imageName

                #cv2.imshow('main', binaryImage)
                cv2.imwrite(binaryImgName, binaryImage)

                #Get pixels in image and resize image
                im = Image.open(binaryImgName)
                im.thumbnail((100,150), Image.ANTIALIAS)
                im.save(binaryImgName)

                pixels = list(im.getdata())
                imagePixelList.append(pixels)

                # Debug print statement - pixel array
                #print(pixels)

                #Write CSV file with shape data
                fl = open('shapeData.csv', 'w')

                writer = csv.writer(fl, lineterminator='\n')

                for key, val in enumerate(pixels):
                    labelRow.append('pixel'+str(key))

                writer.writerow(labelRow)

                for key, val in enumerate(imagePixelList):
                    writer.writerow(pixelRow + imagePixelList[key])

                fl.close()
            except IOError:
                print 'IO error caught'

print('Finished generating data')

