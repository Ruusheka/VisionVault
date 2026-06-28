import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')
# cv.imshow('Blank',blank)

#1. paint the image with green
# blank[200:300,300:400]=0,0,255
# cv.imshow('Green',blank)

#2.Rectangle box
# cv.rectangle(blank,(0,0),(250,500),(0,255,0),thickness=2)
# cv.imshow('Rectangle',blank)


#3.filled Rectangle Box
# cv.rectangle(blank,(0,0),(250,500),(0,255,0),thickness=cv.FILLED)
# cv.imshow('Rectangle',blank)
# cv.rectangle(blank,(0,0),(250,500),(0,255,0),thickness=-1)
# cv.imshow('Rectangle',blank)

# cv.rectangle(blank, (0, 0), (blank.shape[1] // 2, blank.shape[0] // 2), (0, 255, 0), thickness=-1)
# cv.imshow('Rectangle',blank)

#4.Circle
# cv.circle(blank,(250,250),80,(0,0,255),thickness=-1)
# cv.imshow('Circle',blank)

#5 Line
# cv.line(blank,(100,250),(blank.shape[1]//2,blank.shape[0]//2),(0,195,255),thickness=3)
# cv.imshow('Line',blank)

# cv.line(blank,(100,250),(300,400),(0,195,255),thickness=3)
# cv.imshow('Line',blank)


#6.Text
cv.putText(blank,'Hello World!! Welcome to XYZ company',(0,225),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2)
cv.imshow('Text',blank)
cv.waitKey(0)