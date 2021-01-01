import numpy as np
import cv2 as cv

def click_event(event, x, y, flags, param):
    if event == cv.EVENT_RBUTTONDOWN:
        Blue = img[y, x, 0]
        Green = img[y, x, 1]
        Red = img[y, x, 2]
        font = cv.FONT_HERSHEY_SIMPLEX
        strBGR = str(Blue) + "," + str(Green) + "," + str(Red)
        cv.putText(img, strBGR, (x, y), font, 1, (0, 255, 255), 2)
        cv.imshow("Image", img)

# img = np.zeros([500, 500, 3], np.uint8)
img = cv.imread("Images/Ronaldo-Kick.jpg")
cv.imshow("Image", img)
cv.setMouseCallback("Image", click_event)

cv.waitKey(0)
cv.destroyAllWindows()