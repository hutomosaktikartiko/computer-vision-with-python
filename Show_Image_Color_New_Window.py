import numpy as np
import cv2 as cv

def click_event(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        Blue = img[y, x, 0]
        Green = img[y, x, 1]
        Red = img[y, x, 2]
        ImageColor = np.zeros((300, 300, 3), np.uint8)
        ImageColor[:] = [Blue, Green, Red]

        cv.imshow("BGR COLORS", ImageColor)

img = cv.imread("Images/Color-Balls-2.jpg")
cv.imshow("Image", img)

cv.setMouseCallback("Image",  click_event)

cv.waitKey(0)
cv.destroyAllWindows()