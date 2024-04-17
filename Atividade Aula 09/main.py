import numpy as np
import cv2

img = cv2.imread('images/clown2.jpg', cv2.IMREAD_GRAYSCALE)

dft = np.fft.fft2(img)
dft_shift = np.fft.fftshift(dft)
magnitude_spectrum = np.log(np.abs(dft_shift))/20
mask = np.ones_like(img) * 255

# definindo os pontos
coordinates = [(290, 228), (229, 242), (208, 277), (271, 265)]
radius = 6
color = (0, 0, 0)
thickness = -1
for coord in coordinates:
    mask = cv2.circle(mask, coord, radius, color, thickness)

#blur gaussiano
mask = cv2.GaussianBlur(mask, (11, 11), 0)

magnitude_spectrum = np.multiply(magnitude_spectrum, mask/255)

dft_shift_masked = np.multiply(dft_shift,mask) / 255
back_ishift = np.fft.ifftshift(dft_shift)
back_ishift_masked = np.fft.ifftshift(dft_shift_masked)

img_filtered = np.fft.ifft2(back_ishift_masked)
img_filtered = np.abs(img_filtered).clip(0,255).astype(np.uint8)

cv2.imshow("Imagem", img)
cv2.imshow("Espectro", magnitude_spectrum)
cv2.imshow("Mascara", mask)
cv2.imshow("Imagem Filtrada", img_filtered)
cv2.waitKey(0)
cv2.destroyAllWindows()