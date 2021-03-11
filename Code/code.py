import cv2

# File Path to Image
image = cv2.imread('../Images/image1.jpg', 0)
# Set Up Window
cv2.imshow('Digital Image Processing', image)

key = cv2.waitKey(0)
# Exit Keys (Esc - Quit) (S - Save and Quit)
if key == 27:
    cv2.destroyAllWindows()
elif key == ord('s'):
    cv2.imwrite('../Images/saved_image.png', image)
    cv2.destroyAllWindows()
