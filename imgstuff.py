import cv2
import numpy as np
import os


def grays(num):
    try:
        img = cv2.imread("all pics/" + str(num) + ".jpg", cv2.IMREAD_GRAYSCALE)
        resized = cv2.resize(img, (100, 100))
        cv2.imwrite("negative/" + str(num) + ".jpg", resized)
        num += 1
    except:
        pass


for i in range(85,1085):
    grays(i)
