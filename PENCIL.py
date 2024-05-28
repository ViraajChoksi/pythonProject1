import cv2 as cv
import numpy as np

img = cv.imread('Laser 2.jpg')
img1 =cv.resize(img, (500,500),interpolation= cv.INTER_AREA )
cv.imshow('img', img1)

gray = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

sobelx = cv.Sobel(gray,cv.CV_64F,1,0)
sobely = cv.Sobel(gray,cv.CV_64F,0,1)
sobelx = np.uint8(np.absolute(sobelx))
sobely = np.uint8(np.absolute(sobely))
combined = cv.bitwise_or(sobelx,sobely)
cv.imshow('sobelx', sobelx)
cv.imshow('sobely', sobely)
cv.imshow('sobelxy', combined)

canny = cv.Canny(gray, 150,175)
cv.imshow('canny', canny)


cv.waitKey(0)