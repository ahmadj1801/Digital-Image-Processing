import argparse as ap
import cv2
import sys


# Callback Function - On Left Click
def on_left_click(event, x, y, flags, param):
    # Using the image defined
    global image, image_matrix
    # Check for Left Click
    if event == cv2.EVENT_LBUTTONDOWN:
        # OpenCV uses Colours as BGR
        blue, green, red = image[y, x]
        print('<R, G, B> Values at [{}, {}] = <{}, {}, {}>'.format(x, y, red, green, blue))
        print('From Picture:', red, 'From Matrix:', image_matrix[y][x])


def set_intensity_matrix():
    global image, image_matrix
    a = image.shape[0]
    b = image.shape[1]
    for y in range(0, a):
        arr = []
        for x in range(0, b):
            arr.append(image[y, x][0])
        image_matrix.append(arr)


def print_intensity_matrix():
    global image_matrix
    for row in image_matrix:
        print(row)


# Intensity Matrix
image_matrix = []
# Path to image/gif/video
media_path = '../Images/maradona.jpg'
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
    print('(Rows, Columns, Channels) = ', image.shape)
    print('Number of Pixels = ', image.size)
    print('Pixel Depth = ', image.dtype)
    # Set the Matrix
    set_intensity_matrix()
    print_intensity_matrix()
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
