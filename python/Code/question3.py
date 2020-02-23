import cv2

img = cv2.imread("../inputimage/q1inputimage.jpeg")

redimage = img[:, :, 2]
greenimage = img[:, :, 1]
blueimage =img[:, :, 0]


cv2.imwrite("../outputimage/q3redimage.png", redimage)
cv2.imwrite("../outputimage/q3greenimage.png", greenimage)
cv2.imwrite("../outputimage/q3blueimage.png", blueimage)


