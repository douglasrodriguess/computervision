import cv2

image = cv2.imread("../inputimage/q1inputimage.jpeg")
grayimage = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

cannyimage = cv2.Canny(grayimage, 100, 102)
# Se o gradiente de intensidade de pixel for maior que 200, ele será considerado como pixel de bordas
# Se o gradiente de intensidade de pixel for menor que 50, ele não será considerado como pixel de bordas
# Se o gradiente de intensidade de pixel estiver entre 50 e 200, ele só será considerado como pixel de borda se estiver
#   conectado com outro pixel no qual o seu valor é maior que 200.

cv2.imwrite("../outputimage/q6outputimage.png", cannyimage)

cv2.imshow("View", cannyimage)
cv2.waitKey(0)


































