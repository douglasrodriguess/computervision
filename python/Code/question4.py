import cv2

img = cv2.imread("../inputimage/q1inputimage.jpeg")

HSVimg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow("View", HSVimg)
cv2.waitKey(0)

cv2.imwrite("../outputimage/q4HSVimage.png", HSVimg)

Himg = HSVimg[:, :, 2]
Simg = HSVimg[:, :, 2]
Vimg = HSVimg[:, :, 2]

cv2.imwrite("../outputimage/q4HVimage.png", Himg)
cv2.imwrite("../outputimage/q4Simage.png", Simg)
cv2.imwrite("../outputimage/q4Vimage.png", Vimg)
