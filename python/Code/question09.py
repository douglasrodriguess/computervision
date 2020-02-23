import cv2

image = cv2.imread("../inputimage/q1inputimage.jpeg")
grayimage = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

sizeX, sizeY = grayimage.shape[:2]
print(sizeX, sizeY)

with open ("../outputimage/pixelquestion9.txt", "w") as file:
    for rows in range(sizeX):
        for columns in range(sizeY):
            file.write(str(grayimage[rows, columns]) + ' ')
        file.write("\n")
