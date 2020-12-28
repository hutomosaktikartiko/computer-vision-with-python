import cv2 as cv
import datetime

cap = cv.VideoCapture(0, cv.CAP_DSHOW)

while(cap.isOpened()):
    ret, frame = cap.read()

    if ret == True:
        font = cv.FONT_HERSHEY_SIMPLEX
        text = "Width: " + str(cap.get(3)) + "    Height: " + str(cap.get(4))
        currentDate = str(datetime.datetime.now())
        FRAME = cv.putText(frame, currentDate, (10, 50), font, 1, (0, 255, 255), 2, cv.LINE_AA)
        cv.imshow("Frame", frame)

        if cv.waitKey(1) & 0xFF == ord("e"):
            break

cap.release()
cv.destroyAllWindows()