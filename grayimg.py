import cv2


c = 0
def grays(num, c):
    try:
        img = cv2.imread("all pics/" + str(num) + ".jpg", cv2.IMREAD_GRAYSCALE)
        resized = cv2.resize(img, (100, 100))
        cv2.imwrite("neg1/" + str(1000 + num + c) + ".jpg", resized)
        return 0
    except:
        return -1


for i in range(1085):
    c += grays(i, c)
