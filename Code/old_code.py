
# python code.py -i image.png

# Set Up parameters from console
""" parser = ap.ArgumentParser()
parser.add_argument('-i', '--image', required=True, help='Insert Image Name')
args = vars(parser.parse_args())
image_path = args['image']
image_path = '../Images/'+image_path

# Path to Image
image_path = '../Images/graph.gif'

extension = image_path[-3::]
if extension == "mp4" or extension == "gif":
    vid = cv2.VideoCapture(image_path)
    while vid.isOpened():
        ret, frame = vid.read()
        if ret:
            cv2.imshow('Digital Image Processing', frame)
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break
    vid.release()
else:
    # File Path to Image
    image = cv2.imread(image_path, 0)
    # Set Up Window
    cv2.imshow('Digital Image Processing', image)

    key = cv2.waitKey(0)
    # Exit Keys (q - Quit) (S - Save and Quit)
    if key == ord('q'):
        cv2.destroyAllWindows()
    elif key == ord('s'):
        cv2.imwrite('../Images/saved_image.png', image)
        cv2.destroyAllWindows()
"""