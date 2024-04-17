import cv2
import numpy as np

img = cv2.imread('images/img.jpg')
img_mask = cv2.imread('images/logo.png', cv2.IMREAD_UNCHANGED)

mask_height, mask_width = img_mask.shape[:2]

top_left = (0, 0)  

b, g, r, alpha = cv2.split(img_mask)

img_mask_rgb = cv2.merge((b, g, r))

alpha_mask = cv2.merge((alpha, alpha, alpha))

region = img[top_left[1]:top_left[1]+mask_height, top_left[0]:top_left[0]+mask_width]
masked_region = cv2.bitwise_and(region, 255 - alpha_mask)
masked_logo = cv2.bitwise_and(img_mask_rgb, alpha_mask)
combined = cv2.add(masked_region, masked_logo)

img[top_left[1]:top_left[1]+mask_height, top_left[0]:top_left[0]+mask_width] = combined

mask = np.zeros_like(img)

alpha_3channel = cv2.cvtColor(alpha, cv2.COLOR_GRAY2BGR)

mask[top_left[1]:top_left[1]+mask_height, top_left[0]:top_left[0]+mask_width] = alpha_3channel

mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)

telea = cv2.inpaint(img, mask, 3, cv2.INPAINT_TELEA)
ns = cv2.inpaint(img, mask, 3, cv2.INPAINT_NS)

cv2.imshow('Image with Logo', img)
cv2.imshow('roi', combined)
cv2.imshow('telea.png', telea)
cv2.imshow('ns.png', ns)

cv2.waitKey(0)
