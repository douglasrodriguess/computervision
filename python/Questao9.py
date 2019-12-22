import cv2
import numpy as np

imagem = cv2.imread('imagem.jpg')

imagemgray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

rows, cols = imagemgray.shape[:2]

print ("\nLinhas: ", rows)
print ("\nColunas: ", cols)

with open ('pixels.txt', 'w') as file:
    for row in range (rows):
        for column in range (cols):
            file.write (str(imagemgray[row, column]) + ' ')
        file.write ('\n')