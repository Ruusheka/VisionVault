import cv2 as cv

img = cv.imread('photos/group 1.jpg')
# cv.imshow('Cat',img)

#converting from bgr to gray scale image
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('Grey',gray)

#blur
blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
# cv.imshow('Blur',blur)

#Edge Cascade
canny = cv.Canny(img,125,175)
# cv.imshow('Edge Cascade',canny)

#dialating the image
dilated = cv.dilate(canny,(3,3),iterations=1)
# cv.imshow('Dilated',dilated)

dilated2 = cv.dilate(canny,(7,7),iterations=3)
# cv.imshow('Dilated2',dilated2)

#eroded
eroded = cv.erode(dilated2,(7,7),iterations=3)
# cv.imshow('Eroded',eroded)

#resize image
resized = cv.resize(img,(500,500),interpolation = cv.INTER_CUBIC)
cv.imshow('Resize',resized)

#cropped image
cropped = img[50:200,200:400]
cv.imshow('Cropped',cropped)



cv.waitKey(0)