import cv2
import numpy as np

imagem = cv2.imread ('imagem.jpg')

imagemHSV = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

cv2.imshow("HSV", imagemHSV)
cv2.waitKey(0)

Hchannel, Schannel, Vchannel = cv2.split(imagem)

cv2.imshow("H Channel", Hchannel)
cv2.waitKey(0)
cv2.imshow("S Channel", Schannel)
cv2.waitKey(0)
cv2.imshow("V Channel", Vchannel)
cv2.waitKey(0)


