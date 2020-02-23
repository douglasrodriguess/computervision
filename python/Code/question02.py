import cv2

image = cv2.imread("../inputimage/q1inputimage.jpeg")
grayimage = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
cv2.imshow("View", grayimage)
cv2.waitKey(0)
cv2.imwrite("../outputimage/q2outputimage.png", grayimage)










