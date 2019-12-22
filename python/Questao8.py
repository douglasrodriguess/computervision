import cv2

imagem = cv2.imread('imagem.jpg')

width = imagem.shape[1]
heigth = imagem.shape[0]

imagemmenor = cv2.resize (imagem, (width, heigth))
cv2.imshow("imagem resize", imagemmenor)
cv2.waitKey(0)