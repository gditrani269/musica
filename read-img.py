import cv2
import numpy as np
import matplotlib.pyplot as plt

imagen = cv2.imread("partitura2.png")
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

_, umbral = cv2.threshold(
    gris,
    150,
    255,
    cv2.THRESH_BINARY_INV
)

# Kernel horizontal
kernel = cv2.getStructuringElement(
    cv2.MORPH_RECT,
    (50,1)
)

# Detectar líneas horizontales
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (80,1))

horizontal = cv2.morphologyEx(
    umbral,
    cv2.MORPH_OPEN,
    kernel
)

plt.figure(figsize=(14,8))
plt.imshow(horizontal, cmap="gray")
plt.title("Líneas horizontales")
plt.show()

contornos, _ = cv2.findContours(
    horizontal,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

for c in contornos:

    x,y,w,h = cv2.boundingRect(c)

    if w > 300:      # ajustar según la imagen
        print(y)