import cv2

imagem = cv2.imread('imagem.jpg')

cv2.imshow('Imagem de entrada', imagem)
cv2.waitKey(0)

imagemgray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

cv2.imshow('Imagem em tons de cinza', imagemgray)
cv2.waitKey(0)

cv2.imwrite('imagememtomdecinza.jpg', imagemgray)