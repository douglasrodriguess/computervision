import cv2
import numpy as com

imagem = cv2.imread('imagem.jpg')

imagemgray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

imagemblur = cv2.blur(imagemgray, (3,3))
cv2.imshow("Imagem blur", imagemblur)
cv2.waitKey(0)

imagemmedian = cv2.medianBlur(imagemgray, 5)
cv2.imshow("Imagem mediana", imagemmedian)
cv2.waitKey(0)

compare = com.concatenate ((imagemmedian, imagemblur, imagemgray), axis=1)
cv2.imshow("Imagem para comparação",compare)
cv2.waitKey(0)