from random import randint
import cv2 as cv
import numpy as np

img =cv.imread("images/img.jpg")
cv.namedWindow('new')
img_width, img_height = img.shape[:2]
variation = 5

# resized_img = cv.resize(img, (int(img_width/2), int(img_height/2)))
# cv.imwrite('images/img.jpg', resized_img)

new_img = np.ones((img_height, img_width, 3), dtype=np.uint8) * 255

def apply_noise(img, variation):
    for x in range(0,img_width):
        for y in range(0,img_height):
            num = np.random.randint(0, 100)
            if num < variation: 
                new_img[y][x] = [0, 0, 0]
            elif num > 100 - variation:
                new_img[y][x] = [255, 255, 255]	
            else:
                new_img[y][x] = img[y][x]

apply_noise(img, variation)
while True:
    cv.imshow('new',new_img)
    if cv.waitKey(20) & 0xFF == ord('q'):
        break
    if cv.waitKey(20) & 0xFF == ord('w'):
        variation += 3
        print(f'Porcentagem de Noise:{variation*2}')
        apply_noise(img, variation)
    if cv.waitKey(20) & 0xFF == ord('s'):
        variation -= 3
        print(f'Porcentagem de Noise:{variation*2}')
        apply_noise(img, variation)

cv.imshow('new',new_img)

cv.waitKey(0)
cv.destroyAllWindows()
