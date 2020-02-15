#!/usr/bin/python

from PIL import Image
import sys

size = 100

if len(sys.argv) == 1:
    print("Usage: ./aI.py /path/to/image.png")
    sys.exit()
image = Image.open(sys.argv[1])
image = image.resize((size,size))
pixels = image.load()


height = size
width = size

y = 0
x = 0

colors = (".",";","#","$")
currentPixelRow = ""
while y < height:
    while x < width:
        pixel = pixels[x,y]
        x += 1
        brightness = (pixel[0] + pixel[1] + pixel[2]) / 3
        if brightness <= 64:
            currentPixelRow += colors[0]
            currentPixelRow += colors[0]
        elif brightness > 64 and brightness <= 128:
            currentPixelRow += colors[1]
            currentPixelRow += colors[1]
        elif brightness > 128 and brightness <= 192:
            currentPixelRow += colors[2]
            currentPixelRow += colors[2]
        else:
            currentPixelRow += colors[3]
            currentPixelRow += colors[3]
    
    #print(len(currentPixelRow))
    print(currentPixelRow)
    currentPixelRow = ""
    x = 0
    y += 1

