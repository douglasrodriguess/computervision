import cv2

imagem = cv2.imread('imagem.jpg')
cv2.imshow('Imagem de entrada', imagem)
cv2.waitKey(0)

bluechannel, greenchannel, redchannel = cv2.split(imagem)

cv2.imshow('red channel', redchannel)
cv2.waitKey(0)
cv2.imshow('green channel', greenchannel)
cv2.waitKey(0)
cv2.imshow('blue channel', bluechannel)
cv2.waitKey(0)

