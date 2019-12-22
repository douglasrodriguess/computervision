import cv2

imagem = cv2.imread ('imagem.jpg')

imagemgray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

ret, imagelimiarizada = cv2.threshold(imagemgray, 127, 255, cv2.THRESH_BINARY)

matriz = imagemgray.copy()
rows, cols = imagem.shape[:2]

with open('pixels.txt', 'w') as file:
    for row in range (rows):
        for col in range (cols):
            file.write(str(imagelimiarizada[row, col]) + ' ')
        file.write('\n')


