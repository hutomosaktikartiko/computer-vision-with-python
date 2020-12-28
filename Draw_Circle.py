import cv2 as cv

img = cv.imread("Images/Ronaldo-1.jpg")

cv.circle(img, (100, 100), 100, (0, 255, 0), thickness=10)

cv.imshow("Image", img)

cv.waitKey(0)
cv.destroyAllWindows()