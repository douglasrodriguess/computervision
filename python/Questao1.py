import cv2

imagem = cv2.imread('imagem.jpg')

print("\nExibindo a imagem...\n")

cv2.imshow('Exibir a imagem', imagem)
cv2.waitKey(0)

print("\nSalvando a imagem...\n")
cv2.imwrite('imagemsalvada.jpg', imagem)

