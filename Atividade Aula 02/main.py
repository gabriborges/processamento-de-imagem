import cv2 as cv
import numpy as np

def grey_scale(pixel):
    return (pixel[0] + pixel[1] + pixel[2]) / 3

img = cv.imread('images/color_red.jpg')
img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
img_grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
final = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)

x, y = img_hsv.shape[0:2]

for row in range(x):
    for col in range(y):
        if img_hsv[row, col][0] < 170 or img_hsv[row, col][0] > 200:
            final[row, col] = img_grey[row, col]
        else: 
            final[row, col] = img[row, col]

cv.imshow('Imagem Cinza', final)

cv.waitKey(0)
cv.destroyAllWindows()