import cv2 as cv
#import DILPREET1910_Mediapipe as mp


vid = cv.VideoCapture(0)

#mpHands = mp.solutions.hands
#hands = mpHands.hands()
while True:
    ma,img = vid.read()
    rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    cv.imshow("img", rgb)
    vid.get(17)

    cv.waitKey(27)