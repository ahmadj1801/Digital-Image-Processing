import argparse as ap
import cv2
import sys


# Callback Function - On Left Click
def on_left_click(event, x, y, flags, param):
    # Using the image defined
    global image
    # Check for Left Click
    if event == cv2.EVENT_LBUTTONDOWN:
        # OpenCV uses Colours as BGR
        blue, green, red = image[y, x]
        print('<R, G, B> Values at [{}, {}] = <{}, {}, {}>'.format(x, y, red, green, blue))


# Path to image/gif/video
media_path = '../Images/f1.jpeg'
# Extract the file extension
extension = media_path[-3::]
# Video formats
video_formats = ['gif', 'mp4']

# Check if it is an image or not
if extension not in video_formats:
    # IMAGE
    cv2.namedWindow("Digital Image Processing")
    cv2.setMouseCallback("Digital Image Processing", on_left_click)
    image = cv2.imread(media_path)
    # Display
    while True:
        cv2.imshow("Digital Image Processing", image)
        # Key to Exit
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
else:
    # GIF/VIDEO
    window = cv2.VideoCapture(media_path)
    if not window.isOpened():
        print('Failed To Open!')
        sys.exit()

    # Loop gif/video
    while window.isOpened():
        ret, frame = window.read()
        if ret:
            img = cv2.imshow('Digital Image Processing', frame)

        else:
            window.set(cv2.CAP_PROP_POS_FRAMES, 0)

        # Exit Key
        key = cv2.waitKey(1)
        if key == ord('q'):
            # Release the gif/video
            window.release()
            break

# Close open windows
cv2.destroyAllWindows()
