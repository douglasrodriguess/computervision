import cv2
import numpy

image = cv2.imread("../inputimage/q1inputimage.jpeg")
grayimage = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

sizeX, sizeY = grayimage.shape[:2]
print(sizeX, sizeY)

thresh = 100

with open ("../outputimage/pixelquestion10.txt", "w") as file:
    for rows in range(sizeX):
        for columns in range(sizeY):
            if (grayimage[rows, columns] > thresh):
                file.write('255' + ' ')
            else:
                file.write('0' + ' ')
        file.write("\n")
