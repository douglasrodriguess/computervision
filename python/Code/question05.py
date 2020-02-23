import cv2

image = cv2.imread("../inputimage/q1inputimage.jpeg")
grayimage = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)


blur = cv2.blur(grayimage, (5, 5))

cv2.imwrite("../outputimage/q5bluroutputimage.png", blur)

medianimage = cv2.medianBlur(grayimage, 5)

cv2.imwrite("../outputimage/q5medianoutputimage.png", medianimage)

cv2.imshow("View", medianimage)
cv2.waitKey(0)










