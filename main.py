import cv2 as cv

img = cv.imread('Laser 2.jpg')
cv.imshow('img', img)

average = cv.blur(img, (3,3))
cv.imshow('average',average)

gaussian= cv.GaussianBlur(img,(5,5),0)
cv.imshow('gaussian',gaussian)

median= cv.medianBlur(img,7)
cv.imshow('median', median)

bilateral= cv.bilateralFilter(img, 5 ,15, 15)
cv.imshow('bilateral', bilateral)

cv.waitKey(0)
