import cv2



def grays(num):
    try:
        img = cv2.imread("all pics/" + str(num) + ".jpg", cv2.IMREAD_GRAYSCALE)
        resized = cv2.resize(img, (100, 100))
        cv2.imwrite("negative/" + str(num) + ".jpg", resized)
    except:
        pass


for i in range(1085):
    grays(i)
