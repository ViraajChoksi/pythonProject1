import cv2 as cv
import numpy as np

blank = np.zeros((500,1000,3),dtype ='uint8')
#cv.imshow('blank', blank)

#blank[:] = 0,50,255
#cv.imshow('Green', blank)
cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,250,0),thickness=5)
cv.rectangle(blank,(0,0),(250,250),(0,0,250), thickness=-1)
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,250,0),thickness=2)
cv.putText(blank,'Hello',(250,250),5 , 4.0,(255,0,0),5)
cv.imshow('rectange',blank)
cv.waitKey(0)
