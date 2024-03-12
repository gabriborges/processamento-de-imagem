import cv2 as cv
import numpy as np

img = cv.imread('images/img.jpg')

rows, cols = img.shape[:2]
rotation_x , rotation_y = (cols-1)/2.0, (rows-1)/2.0
angle = 0
img_copy = img.copy()

M = cv.getRotationMatrix2D((rotation_x, rotation_y), angle, 1)
res = cv.warpAffine(img_copy, M, (cols, rows))
  
cv.namedWindow('res')

while True:
    angle = 0
    cv.imshow('res', res)
    img_copy = res
    
    if cv.waitKey(10) & 0xFF == 27:
        break
    elif cv.waitKey(20) & 0xFF == ord('r'):
        angle+=10
        M = cv.getRotationMatrix2D((rotation_x, rotation_y), angle, 1)
        res = cv.warpAffine(img_copy, M, (cols, rows))
   
cv.imshow('res', res)

cv.waitKey(0)
cv.destroyAllWindows()