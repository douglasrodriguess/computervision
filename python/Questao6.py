import cv2

imagem = cv2.imread ('imagem.jpg')

imagemgray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

imagembordas = cv2.Canny(imagemgray, 100, 200)

cv2.imshow("Imagem Bordas", imagembordas)
cv2.waitKey(0)

