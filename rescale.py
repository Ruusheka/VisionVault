import cv2 as cv

img = cv.imread('photos/cat.jpg')
cv.imshow('Cat',img)

def changeRes(width,height):
    #for live video
    capture.set(3,width)
    capture.set(4,height)
    
    
def rescaleFrame(frame,scale=.75):
    #for images,videos and live video
    width=int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dim =(width,height)
    return cv.resize(frame,dim,interpolation=cv.INTER_AREA)


# resizing image
resized_image = rescaleFrame(img)
cv.imshow('Image',resized_image)

#resizing video
capture=cv.VideoCapture('videos/dog.mp4')
while True:
    isTrue,frame = capture.read()
    frame_resized = rescaleFrame(frame)
    
    cv.imshow('Video',frame)
    cv.imshow('Video Resized',frame_resized)
    
    if cv.waitKey(20) & 0xFF==ord('d'):  #if d is pressed, the video is stopped
        break
    
capture.release()
cv.destroyAllWindows()