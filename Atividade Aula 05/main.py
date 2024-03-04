# coding=utf-8
import cv2
import numpy as np

imagem = cv2.imread('images/img.jpg')

def ajuste_brilho(img, br, mode):
    brilho=[br,br,br]
    res=np.zeros(img.shape, np.uint8)
    for y in range(0, img.shape[0]):
        for x in range(0, img.shape[1]):
            if mode == 'add':
                res[y, x] = np.minimum(img[y,x]+brilho,[255,255,255])
            else:
                res[y, x] = np.maximum(img[y, x]+brilho, [0, 0, 0])
    return res

def ajuste_constraste(img, con):
    res = np.zeros(img.shape, np.uint8)
    for y in range(0, img.shape[0]):
        for x in range(0, img.shape[1]):
            res[y, x] = np.minimum(img[y, x]*con, [255, 255, 255])
    return res

def negativo(img):
    res = np.zeros(img.shape, np.uint8)
    for y in range(0, img.shape[0]):
        for x in range(0, img.shape[1]):
            res[y, x] = 255-img[y, x]
    return res

cv2.namedWindow('Brilho')
brilho=0
contraste = 1
result=imagem

while(True):
    cv2.imshow('Brilho',result)
    k=cv2.waitKey(20)
    if k == 27:
        break
    elif k == ord('a'):
        brilho+=20
        result=ajuste_brilho(imagem,brilho, 'add')
    elif k == ord('z'):
        brilho-=20
        result=ajuste_brilho(imagem,brilho, 'sub')
    elif k == ord('s'):
        contraste+=0.1
        result=ajuste_constraste(imagem,contraste)
    elif k == ord('x'):
        contraste-=0.1
        result=ajuste_constraste(imagem,contraste)
    elif k == ord('n'):
        result = negativo(imagem)


cv2.destroyAllWindows()