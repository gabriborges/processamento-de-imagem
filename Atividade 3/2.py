from random import randint
import cv2 as cv
import numpy as np

img =cv.imread("images/exe.jpg")
img_width, img_height = img.shape[:2]

print(img_width, img_height)
print(img[0][0].sum())

new_img = np.ones((img_height//3, img_width//3, 3), dtype=np.uint8) * 255

def get_average(img, x, y):
    sum = img[y-1,x-1].sum()+img[y-1,x].sum() + img[y,x-1].sum() + img[y,x].sum() + img[y+1,x-1].sum() + img[y+1,x].sum() + img[y,x+1].sum() + img[y+1,x+1].sum() + img[y-1,x+1].sum()
    sum = sum//9//3
    return [sum, sum, sum]

for x in range(1,img_width,3):
    for y in range(1,img_height,3):
        new_img[y//3][x//3] = get_average(img, x, y)

cv.imshow('photo',img)
cv.imshow('new',new_img)

cv.waitKey(0)
cv.destroyAllWindows()