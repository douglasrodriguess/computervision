import cv2

image = cv2.imread("../inputimage/q1inputimage.jpeg")
cv2.imshow("view", image)
cv2.waitKey(0)
cv2.imwrite("../outputimage/q1outputimage.png", image)

