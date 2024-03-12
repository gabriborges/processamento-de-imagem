import cv2 as cv
import numpy as np

img = cv.imread('images/img.jpg')

angle = 10
img_width, img_height = img.shape[:2]
rotation_x , rotation_y = (img_height-1)/2.0, (img_width-1)/2.0

res = np.zeros((img_height, img_width, 3), np.uint8)
M = cv.getRotationMatrix2D((rotation_x, rotation_y), angle, 1)

def multiply_matrix(matrix, pixel):
    pixel = np.array([pixel[0], pixel[1], 1])
    matrix = np.vstack([matrix, [0, 0, 1]])
    result = np.dot(matrix, pixel)
    result = (int(np.round(result[0] / result[2])), int(np.round(result[1] / result[2])))
    
    return result

def apply_transformation(pixel_before, pixel_after):
    global res
    if pixel_after[0] >= 0 and pixel_after[0] < img_width and pixel_after[1] >= 0 and pixel_after[1] < img_height:
        res[pixel_after[0], pixel_after[1]] = img[pixel_before[0], pixel_before[1]]

print("Processando...")
#itera sobre os pixels
for width in range(img_width):
    for height in range(img_height):
        apply_transformation((width, height), multiply_matrix(M, (width, height)))

cv.imshow('res', res)

cv.waitKey(0)
cv.destroyAllWindows()