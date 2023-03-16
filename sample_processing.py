import cv2


def pros(num):
    try:
        img = cv2.imread("samples/IMG-" + str(2336 + num) + ".jpg", cv2.IMREAD_GRAYSCALE)
        resized = cv2.resize(img, (50, 50))
        cv2.imwrite("processed_samples/" + str(num) + ".jpg", resized)
    except:
        pass


for i in range(5):
    pros(i)
