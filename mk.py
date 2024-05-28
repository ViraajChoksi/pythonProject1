import cv2 as cv

img = cv.imread('Laser 2.jpg')
img1=cv.resize(img,(500,500), interpolation=cv.INTER_AREA)

cv.imshow('img1', img1)

average = cv.blur(img1, (3,3))
cv.imshow('average',average)

gaussian= cv.GaussianBlur(img1,(5,5),0)
cv.imshow('gaussian',gaussian)

median= cv.medianBlur(img1,7)
cv.imshow('median', median)

bilateral= cv.bilateralFilter(img1, 5 ,15, 15)
cv.imshow('bilateral', bilateral)

cv.waitKey(0)