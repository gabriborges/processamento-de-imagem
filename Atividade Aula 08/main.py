import cv2
import numpy as np


def apply_median_filter(image, kernel_size):
    
    # adiciona uma borda a imagem para que o kernel possa ser aplicado nas bordas
    pad_size = kernel_size // 2
    padded_image = cv2.copyMakeBorder(image, pad_size, pad_size, pad_size, pad_size, cv2.BORDER_REFLECT)
    
    if kernel_size % 2 == 0:
        print("O tamanho do kernel deve ser ímpar")
  
    height, width = padded_image.shape[:2] 

    filtered_image = padded_image.copy()

    k = (kernel_size - 1) // 2

    if k>0:
        print('Processando...')      
        for y in range(pad_size, height - pad_size):
            for x in range(pad_size, width - pad_size):

                neighbors, channel_0, channel_1, channel_2 = [], [], [], []
                
                for size in range(1, k+1):
                        items= [padded_image[y-size, x-size], padded_image[y-size, x], padded_image[y-size, x+size], padded_image[y, x-size], padded_image[y, x], padded_image[y, x+size], padded_image[y+size, x-size], padded_image[y+size, x], padded_image[y+size, x+size]]
                        neighbors.extend(items)     

                channel_0 = [pixel[0] for pixel in neighbors]
                channel_1 = [pixel[1] for pixel in neighbors]
                channel_2 = [pixel[2] for pixel in neighbors]

                median_chanel_0, median_channel_1, median_channel_2 = int(np.median(channel_0)), int(np.median(channel_1)), int(np.median(channel_2))
                #print(median_chanel_0, median_channel_1, median_channel_2)
            
                filtered_image[y, x][0] = median_chanel_0
                filtered_image[y, x][1] = median_channel_1
                filtered_image[y, x][2] = median_channel_2

    # remove a borda
    filtered_image = filtered_image[pad_size:-pad_size, pad_size:-pad_size]

    return filtered_image

imagem = cv2.imread('images/image2.png')

if imagem is None:
    print("Erro ao carregar a imagem")
else:
    kernel_size = 9
    imagem_filtrada = apply_median_filter(imagem, kernel_size)

    cv2.imshow(f'Imagem Original, kernel:{kernel_size}x{kernel_size}', imagem)
    cv2.imshow(f'Imagem Filtrada, kernel:{kernel_size}x{kernel_size}', imagem_filtrada)

    cv2.waitKey(0)
    cv2.destroyAllWindows()