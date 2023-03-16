import numpy as np
import cv2

cheezit_cascade = cv2.CascadeClassifier('C:/Users/Billy Wei/OneDrive/Documents/GitHub/cheez-it-haar-cascade/data/cascade.xml')

cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # add this
    # image, reject levels level weights.
    cheezit = cheezit_cascade.detectMultiScale(gray, 50, 50)

    # add this
    for (x, y, w, h) in cheezit:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)



    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()