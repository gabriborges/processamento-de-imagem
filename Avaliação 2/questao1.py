import cv2
import numpy as np

img = cv2.imread('images/image.png', cv2.IMREAD_GRAYSCALE)

kernel7 = np.ones((7, 7), np.uint8)
gradient7 = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel7)

kernel3 = np.ones((3, 3), np.uint8)
gradient3 = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel3)

dilation = cv2.dilate(img, kernel7, iterations=1)

cv2.imshow('Original Image', img)
cv2.imshow('Morphological Gradient 7x7', gradient7)
cv2.imshow('Morphological Gradient 3x3', gradient3)
cv2.imshow('Dilation 7x7', dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()