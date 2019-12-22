import cv2

imagem = cv2.imread ('imagem.jpg')

imagemgray = cv2.cvtColor (imagem, cv2.COLOR_BGR2GRAY)

ret, imagemlimiar = cv2.threshold(imagemgray, 127, 255, cv2.THRESH_BINARY)

cv2.imshow('Imagem Threshold', imagemlimiar)
cv2.waitKey(0)