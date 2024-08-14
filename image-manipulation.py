import cv2

# Read an image as greyscale
image = cv2.imread('demo_images/gameplay.jpg', cv2.IMREAD_GRAYSCALE)

# Save the image
cv2.imwrite('demo_images/gameplay-greyscale.jpg', image)

# Read an image as HSV
image = cv2.imread('demo_images/gameplay.jpg', cv2.COLOR_BGR2HSV)

# Save the image
cv2.imwrite('demo_images/gameplay-hsv.jpg', image)

 