import numpy as np
import cv2 as cv

img1 = np.zeros((200, 400, 3), np.uint8)
img1 = cv.rectangle(img1, (100, 25), (300, 150), (250, 255, 255), -1)
img2 = cv.imread("Images/BlackWhite.jpg")

# bitAND = cv.bitwise_and(img1, img2)
# bitOR = cv.bitwise_or(img1, img2)
# bitXOR = cv.bitwise_xor(img1, img2)
bitNOT = cv.bitwise_not(img2)

cv.imshow("Image Output", bitNOT)

cv.waitKey(0)
cv.destroyAllWindows()