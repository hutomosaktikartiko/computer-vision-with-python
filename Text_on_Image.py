import cv2 as cv

img = cv.imread("Images/Ronaldo-1.jpg")

font = cv.FONT_HERSHEY_SIMPLEX

cv.putText(img, "OpenCV", (50, 100), font, 2.5, (0, 255, 0), 5, cv.LINE_AA)

cv.imshow("Image", img)

cv.waitKey(0)
cv.destroyAllWindows()