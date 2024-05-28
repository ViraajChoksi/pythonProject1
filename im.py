import cv2 as cv
import numpy as np

img = cv.imread('Laser 2.jpg')
img1=cv.resize(img,(250,250), interpolation=cv.INTER_AREA)
cv.imshow('img', img1)

def translate(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = img.shape[1],img.shape[0]
    return cv.warpAffine(img, transMat, dimensions)

def rotate(img,angle,rotPoint=None ):
    (height,width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2,height//2)
        rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
        dimensions = (width,height)

        return cv.warpAffine(img,rotMat,dimensions)
rotated=rotate(img, 45)
translated= translate(img1,100,50)
flip=cv.flip(img1,0 )
cv.imshow('translated', flip)
cv.waitKey(0)