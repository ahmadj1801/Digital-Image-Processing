import argparse as ap
import cv2
import sys
import matplotlib.pyplot as plt
import math


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
    image_matrix = []
    a = image.shape[0]
    b = image.shape[1]
    for y in range(0, a):
        arr = []
        for x in range(0, b):
            arr.append(image[y, x][0])
        image_matrix.append(arr)
    print('Intensity matrix has been set!')


def print_intensity_matrix():
    global image_matrix
    for row in image_matrix:
        print(row)


def init_freq_dict():
    global int_freq
    int_freq = dict().fromkeys(range(0, 256))
    for i in int_freq:
        int_freq[i] = 0


def set_freq_dict():
    global int_freq
    for i in image_matrix:
        for j in i:
            int_freq[j] = int_freq.get(j) + 1
    print('Frequencies have been counted!')


def draw_histogram(freq: dict):
    plt.bar(list(freq.keys()), list(freq.values()), width=0.5)
    plt.title('Frequencies of Pixel Shades')
    plt.xlabel('Pixel Shade')
    plt.ylabel('Frequency')
    plt.show()
    pass


def draw_normalised_histogram():
    pass


def negative_image():
    global image, image_matrix
    a = image.shape[0]
    b = image.shape[1]
    for y in range(0, a):
        for x in range(0, b):
            image[y, x] = 255 - image[y, x][0]
    set_intensity_matrix()
    init_freq_dict()
    set_freq_dict()
    draw_histogram(int_freq)


def threshold_image():
    global image, image_matrix, int_freq
    # Halfway value as the threshold
    global_threshold = 128
    # Rows and Columns
    a = image.shape[0]
    b = image.shape[1]
    for y in range(0, a):
        for x in range(0, b):
            pixel_value = image[y, x][0]
            if pixel_value > global_threshold:
                image[y, x] = 255
            else:
                image[y, x] = 0
    set_intensity_matrix()
    init_freq_dict()
    set_freq_dict()
    draw_histogram(int_freq)


def histogram_equalization():
    # Formula = [256/Num Pixels] . [Sum(all intensities until j)]
    global total_pixels, int_freq
    prefix = 255 / total_pixels
    # We have 256 intensities
    # Create and array of 256
    # Iterate through dict and calc values -> convert to int
    # Loop through image pixels and alter according to array
    equalization = []
    for shade in range(0, 256):
        equalization_sum = 0
        for value in range(shade + 1):
            # Equalization Formula
            equalization_sum = equalization_sum + (255 * (int_freq.get(value) / total_pixels))
        # Add to table
        equalization.append(int(round(equalization_sum)))
    # Rows and Columns
    a = image.shape[0]
    b = image.shape[1]
    for y in range(0, a):
        for x in range(0, b):
            # The pixel shade
            pixel_value = image[y, x][0]
            # Look in table to get value
            image[y, x] = equalization[pixel_value]
    set_intensity_matrix()
    init_freq_dict()
    set_freq_dict()
    draw_histogram(int_freq)
    pass


def log_processing():
    global image, int_freq
    row = image.shape[0]
    col = image.shape[1]
    intensities = [(int(45 * math.log(1 + x))) for x in range(0, 256)]
    for y in range(0, row):
        for x in range(0, col):
            shade = image[y, x][0]
            image[y, x] = intensities[shade]
    print(intensities)
    set_intensity_matrix()
    init_freq_dict()
    set_freq_dict()
    draw_histogram(int_freq)
    pass


def gamma_law():
    global image, int_freq
    row = image.shape[0]
    col = image.shape[1]
    intensities = [(int(30 * math.pow(x, 0.4))) for x in range(0, 256)]
    print(intensities)
    for y in range(0, row):
        for x in range(0, col):
            shade = image[y, x][0]
            image[y, x] = intensities[shade]
    set_intensity_matrix()
    init_freq_dict()
    set_freq_dict()
    draw_histogram(int_freq)
    pass


def original_image():
    global image, media_path
    image = cv2.imread(media_path)
    set_intensity_matrix()
    init_freq_dict()
    set_freq_dict()
    draw_histogram(int_freq)


# Intensity Matrix
image_matrix = []
# Histogram Dict
int_freq = dict()
init_freq_dict()

# Path to image/gif/video
media_path = '../Images/leaf.jpg'
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
    total_pixels = image.shape[0] * image.shape[1]
    print('Number of Pixels = ', total_pixels)
    print('Pixel Depth = ', image.dtype)

    # Set the Matrix
    set_intensity_matrix()
    # Count Frequencies
    set_freq_dict()
    # Draw the Histogram based on frequencies per shade
    draw_histogram(int_freq)

    # Display
    while True:
        cv2.imshow("Digital Image Processing", image)
        # Key to Exit
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        elif key == ord('o'):
            original_image()
        elif key == ord('n'):
            negative_image()
        elif key == ord('t'):
            threshold_image()
        elif key == ord('h'):
            histogram_equalization()
        elif key == ord('l'):
            log_processing()
        elif key == ord('g'):
            gamma_law()
        else:
            pass
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
