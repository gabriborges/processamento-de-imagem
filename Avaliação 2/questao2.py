import cv2
import numpy as np

img = cv2.imread('images/image.png', cv2.IMREAD_GRAYSCALE)
img_color = cv2.imread('images/image.png')

edges = cv2.Canny(img, 100, 200)
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    M = cv2.moments(contour)
    
    area = cv2.contourArea(contour)
    perimeter = cv2.arcLength(contour, True)
    
    if perimeter != 0:
        circularity = 4 * np.pi * (area / (perimeter * perimeter))
    else:
        circularity = 0
    print('Circularity:', circularity)
    # O elemento mais circular irá se destacar em relação aos demais que são semelhantes
    if 0.85 < circularity <= 1.0: 
        color = (0, 0, 255)
    else:
        color = (0, 255, 0) 

    cv2.drawContours(img_color, [contour], -1, color, thickness=cv2.FILLED)

cv2.imshow('Original', img)
cv2.imshow('Segmentada e Colorida', img_color)
cv2.waitKey(0)
cv2.destroyAllWindows()