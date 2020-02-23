import cv2

image = cv2.imread("../inputimage/q1inputimage.jpeg")
grayimage = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

ret, thresh = cv2.threshold(grayimage, 127, 255, cv2.THRESH_BINARY)
cv2.imwrite("../outputimage/q7utputimage.png", thresh)

cv2.imshow("View", thresh)
cv2.waitKey(0)

