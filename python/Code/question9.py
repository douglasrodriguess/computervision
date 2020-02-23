import cv2

image = cv2.imread("../inputimage/q1inputimage.jpeg")
grayimage = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

resizeimage = cv2.resize(grayimage, (50, 50))
cv2.imwrite("../outputimage/q8outputimage.png", resizeimage)

cv2.imshow("View", resizeimage)
cv2.waitKey(0)