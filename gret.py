import cv2 as cv
import numpy as np

img = cv.imread('HSFZBN01-E.jpeg')
cv.imshow('img', img)


def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


resized = rescaleFrame(img, scale=0.5)
gray = cv.cvtColor(resized, cv.COLOR_BGR2HSV)=

blur=cv.GaussianBlur(gray,(1,1),cv.BORDER_DEFAULT)
cv.imshow('blu', blur)
canny = cv.Canny(blur, 125,175)
resized1=cv.resize(canny, (1000,1000), interpolation=cv.INTER_AREA)
cropped = gray[0:200,200:400]
cv.imshow('Gray', resized1)
cv.imshow('Gray2', cropped)

cv.waitKey(0)
