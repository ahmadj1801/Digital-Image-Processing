import argparse as ap
import cv2
import sys

media_path = '../Images/maradona.jpg'
window = cv2.VideoCapture(media_path)

if not window.isOpened():
    print('Failed To Open!')
    sys.exit()

while window.isOpened():
    ret, frame = window.read()
    if ret:
        img = cv2.imshow('Digital Image Processing', frame)
    else:
        window.set(cv2.CAP_PROP_POS_FRAMES, 0)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

window.release()
cv2.destroyAllWindows()
sys.exit()

