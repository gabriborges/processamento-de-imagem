from random import randint
import cv2 as cv
import numpy as np

img =cv.imread("images/exe.jpg")
img_width, img_height = img.shape[:2]

print(img_width, img_height)

new_img = np.ones((img_height//3, img_width//3, 3), dtype=np.uint8) * 255

for x in range(1,img_width,3):
    for y in range(1,img_height,3):
        new_img[y//3][x//3] = img[y][x]

cv.imshow('photo',img)
cv.imshow('f',new_img)

cv.waitKey(0)
cv.destroyAllWindows()