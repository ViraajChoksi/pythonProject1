import cv2
import numpy as np

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
out = cv2.VideoWriter('output1.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 15.0, (1280, 720))
ret, frame = cap.read()
avg = np.float64(frame)
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        des = cv2.accumulateWeighted(frame,avg,0.1)
        frameDelta = cv2.absdiff(frame,cv2.convertScaleAbs(avg))
        cv2.imshow('Change in foreground',frameDelta)
        out.write(frameDelta)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

print("Done!!")
cap.release()
out.release()
cv2.destroyAllWindows()