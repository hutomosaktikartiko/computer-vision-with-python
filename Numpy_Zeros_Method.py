import numpy as np
import cv2 as cv

img = np.zeros([512, 512, 3], np.uint8)

img = cv.circle(img, (200, 200), 100, (0, 255, 255), 1)

cv.imshow("Image", img)

cv.waitKey(0)
cv.destroyAllWindows()
