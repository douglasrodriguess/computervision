import cv2
import numpy as np

imagem = cv2.imread('imagem.jpg')

imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

kernel = np.ones((5,5))

imagemresultante = cv2.erode(imagem, kernel, iterations=3)

cv2.imshow('Imagem resultante', imagemresultante)
cv2.waitKey(0)

