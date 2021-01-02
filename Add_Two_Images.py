import cv2 as cv

img1 = cv.imread("Images/Pitch.jpg")
img2 = cv.imread("Images/Ronaldo-Kick.jpg")

img1 = cv.resize(img1, (600, 400))
img2 = cv.resize(img2, (600, 400))

# output = cv.add(img1, img2)

output = cv.addWeighted(img1, .2, img2, 1, 0)

cv.imshow("Image", output)

cv.waitKey(0)
cv.destroyAllWindows()