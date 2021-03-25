import numpy as np
import cv2

cap = cv2.VideoCapture('../Images/maradona.jpg')
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
