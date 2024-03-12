import cv2 as cv
import numpy as np

img = cv.imread('images/img.jpg')

rows, cols = img.shape[:2]
rotation_x , rotation_y = (cols-1)/2.0, (rows-1)/2.0
angle = 0
img_copy = img.copy()

M = cv.getRotationMatrix2D((rotation_x, rotation_y), angle, 1)
res = cv.warpAffine(img, M, (cols, rows))

def set_rotation(event, x, y, flags, param):
    global rotation_x, rotation_y, res
    if event == cv.EVENT_LBUTTONDOWN:
        rotation_x, rotation_y = x, y
        cv.circle(res, (x, y), 2, (0, 0, 255), -1)
        print(rotation_x, rotation_y)
        
cv.namedWindow('res')
M = cv.getRotationMatrix2D((rotation_x, rotation_y), angle, 1)
res = cv.warpAffine(img_copy, M, (cols, rows))

while True:
    angle = 0
    cv.setMouseCallback('res', set_rotation)
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