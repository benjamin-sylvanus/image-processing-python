import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)
while (1):
    # Take each frame
    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    grey = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(
        grey, 200, 255, cv.THRESH_BINARY_INV+cv.THRESH_TRIANGLE)

    # define range of blue color in HSV
    lower_blue = np.array([100, 60, 50])
    upper_blue = np.array([150, 255, 255])
    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_blue, upper_blue)
    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame, frame, mask=mask)
    m = cv.bitwise_and(frame, frame, mask=thresh)
    can = cv.Canny(hsv, 100, 150)
    cv.imshow('frame', frame)
    cv.imshow('mask', mask)
    cv.imshow('res', res)
    cv.imshow('m', m)

    k = cv.waitKey(100)
    if k == 27:
        break
cv.destroyAllWindows()
