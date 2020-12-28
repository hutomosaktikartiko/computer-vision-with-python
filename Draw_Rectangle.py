import cv2 as cv

img = cv.imread("Images/Ronaldo-1.jpg")

cv.rectangle(img, (0, 0), (255, 300), (0, 0, 255), thickness=10)

# Fill Rectangle
cv.rectangle(img, (0, 0), (255, 300), (255, 0, 0), -1)

cv.imshow("Image", img)

cv.waitKey(0)
cv.destroyAllWindows()