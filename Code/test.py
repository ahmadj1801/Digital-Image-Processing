import numpy as np
import cv2
import sys

cap = cv2.VideoCapture('../Images/maradona.jpg')

if not cap.isOpened():
    print('Failed To Open!')
    sys.exit()

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        cv2.imshow("Image", frame)
    else:
        print('no video')
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
sys.exit()
