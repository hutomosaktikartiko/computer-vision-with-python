import cv2 as cv

img = cv.imread("Ronaldo-1.jpg")
print(img)

cv.imshow("Image", img)

cv.waitKey(delay=0)
cv.destroyAllWindows()