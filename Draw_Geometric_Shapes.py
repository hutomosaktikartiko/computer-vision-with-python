import cv2 as cv

img = cv.imread("Images/Messi-Play.jpg", 1)

cv.line(img, (0, 255), (255, 255), (255, 0, 0), thickness=20)
cv.arrowedLine(img, (0, 0), (255, 255), (0, 0, 255), thickness=10)

cv.imshow("Image", img)

cv.waitKey(0)
cv.destroyAllWindows()