# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 22:24:47 2021

@author: FranticUser
"""

# python code to detect shapes part 1
import cv2
import imutils
import numpy as np
from matplotlib import pyplot as plt
  
# reading image
img = cv2.imread('shapes.jpg')
#cv2.imshow('shapes',img)
  
# converting image into grayscale image
gray1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imshow('Middle',gray1)
#blurred = cv2.GaussianBlur(gray1, (5, 5), 0)  #not recomended don't do this!
# setting threshold of gray image
_, threshold = cv2.threshold(gray1, 127, 255, cv2.THRESH_BINARY)
  
# using a findContours() function
contours, _ = cv2.findContours(
    threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#print(contours)
i = 0
  
# list for storing names of shapes
for contour in contours:
  
    # here we are ignoring first counter cause it also detects entire image as as shape
    if i == 0:
        i = 1
        continue
  
    # cv2.approxPloyDP() function to approximate the shape
    approx = cv2.approxPolyDP(
        contour, 0.01 * cv2.arcLength(contour, True), True)
      
    # using drawContours() function
    #cv2.drawContours(img, [contour], 0, (0, 0, 255), 5)
  
    # finding center point of shape
    M = cv2.moments(contour)
    if M['m00'] != 0.0:
        x = int(M['m10']/M['m00'])
        y = int(M['m01']/M['m00'])
    
    #x=approx.ravel()[0]
    #y=approx.ravel()[1]

    # putting shape name at center of each shape
    if len(approx) == 3:
        cv2.putText(img, 'Triangle', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
  
    elif len(approx) == 4:
        #(x,y,w,h) = cv2.boundingRect(approx)
        #ar = w /float(h)
        
        #Name = 'Square' if ar >=0.95 and ar <=1.05 else Rectangle
        cv2.putText(img, 'Quad', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 00,), 2)
  
    elif len(approx) == 5:
        cv2.putText(img, 'Pentagon', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
  
    elif len(approx) == 6:
        cv2.putText(img, 'Hexagon', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
    
    elif len(approx) == 7:
        cv2.putText(img, 'Heptagon', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0, 0), 2)
    
    elif len(approx) == 8:
        cv2.putText(img, 'Octogon', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
        
    #elif 6 < len(approx) < 15:
        #cv2.putText(img, "Ellipse", (x, y), 
                    #cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0 ,0), 2)
    else:
        cv2.putText(img, 'Circle', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
  
# displaying the image after drawing contours
cv2.imshow('shapes', img)
  
cv2.waitKey(0)
cv2.destroyAllWindows()
