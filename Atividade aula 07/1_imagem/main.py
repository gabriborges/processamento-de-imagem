import cv2 as cv
import numpy as np

img = cv.imread('images/img.jpg')
logo = cv.imread('images/logo.jpg')           
img_height, img_width = img.shape[0:2]

logo = cv.resize(logo, (img_width, img_height))
logo_grey = cv.cvtColor(logo, cv.COLOR_BGR2GRAY)

_, mask = cv.threshold(logo_grey, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)

mask_inv = cv.bitwise_not(mask)

logo_fg = cv.bitwise_not(logo, logo, mask = mask_inv)

res = cv.add(img, logo_fg)

cv.imshow('img', res)

cv.waitKey(0)
cv.destroyAllWindows()