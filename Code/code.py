import argparse as ap
import cv2
import sys


def click(event, x, y, flags, param):
    global image
    if event == cv2.EVENT_LBUTTONDBLCLK:
        blue, green, red = image[y, x]
        print('Colours at [', x, ', ', y, '] = < ', red, ', ', green, ', ', blue, ' >')


media_path = '../Images/graph.gif'
extension = media_path[-3::]
video_formats = ['gif', 'mp4']

if extension not in video_formats:
    cv2.namedWindow("Digital Image Processing")
    cv2.setMouseCallback("Digital Image Processing", click)
    image = cv2.imread(media_path)
    while True:
        cv2.imshow("Digital Image Processing", image)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
else:
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
            window.release()
            break

cv2.destroyAllWindows()
sys.exit()

