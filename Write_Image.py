import cv2 as cv

img = cv.imread("Ronaldo-1.jpg", 1)
print(img)

cv.imshow("Image", img)

#Create a new image
cv.imwrite("New-Ronaldo.jpg", img)

cv.waitKey(0)