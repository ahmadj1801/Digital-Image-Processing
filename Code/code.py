import argparse as ap
import cv2

# python code.py -i image.png

# Set Up parameters from console
parser = ap.ArgumentParser()
parser.add_argument('-i', '--image', required=True, help='Insert Image Name')
args = vars(parser.parse_args())
image_path = args['image']
image_path = '../Images/'+image_path

# File Path to Image
image = cv2.imread(image_path, 0)
# Set Up Window
cv2.imshow('Digital Image Processing', image)

key = cv2.waitKey(0)
# Exit Keys (Esc - Quit) (S - Save and Quit)
if key == 27:
    cv2.destroyAllWindows()
elif key == ord('s'):
    cv2.imwrite('../Images/saved_image.png', image)
    cv2.destroyAllWindows()
