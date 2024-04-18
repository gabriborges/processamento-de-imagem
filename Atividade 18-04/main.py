import cv2
import numpy as np

img = cv2.imread('images/cars.png')
mask = np.zeros(img.shape[:2],np.uint8)

bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)

rect = (676,0,1171,470)

cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)

mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')

kernel = np.ones((50,50),np.uint8)
mask_smooth = cv2.morphologyEx(mask2, cv2.MORPH_OPEN, kernel)

foreground = img*mask_smooth[:,:,np.newaxis]
background = img*(1-mask_smooth)[:,:,np.newaxis]

blurred_background = cv2.GaussianBlur(background, (99,99), 0)

final = cv2.add(foreground, blurred_background)

cv2.imshow('img', final)
cv2.waitKey(0)
cv2.destroyAllWindows()