###########################################
## makeBinaryImage.py
###########################################

import numpy as np
import cv2
import csv
import sys, os
from PIL import Image


# python chop.py [chop-factor] [in-file] [out-file]

chop = int(1)
im = Image.open('IMAG19.jpg')
im = im.convert('1')
width, height = im.size
data = im.load()

# Iterate through the rows.
for y in range(height):
    for x in range(width):

        # Make sure we're on a dark pixel.
        if data[x, y] > 120:
            continue

        # Keep a total of non-white contiguous pixels.
        total = 0

        # Check a sequence ranging from x to image.width.
        for c in range(x, width):

            # If the pixel is dark, add it to the total.
            if data[c, y] < 120:
                total += 1

            # If the pixel is light, stop the sequence.
            else:
                break

        # If the total is less than the chop, replace everything with white.
        if total <= chop:
            for c in range(total):
                data[x + c, y] = 255

        # Skip this sequence we just altered.
        x += total


# Iterate through the columns.
for x in range(width):
    for y in range(height):

        # Make sure we're on a dark pixel.
        if data[x, y] > 120:
            continue

        # Keep a total of non-white contiguous pixels.
        total = 0

        # Check a sequence ranging from y to image.height.
        for c in range(y, height):

            # If the pixel is dark, add it to the total.
            if data[x, c] < 120:
                total += 1

            # If the pixel is light, stop the sequence.
            else:
                break

        # If the total is less than the chop, replace everything with white.
        if total <= chop:
            for c in range(total):
                data[x, y + c] = 255

        # Skip this sequence we just altered.
        y += total

im.save('IMAG19result.png')
